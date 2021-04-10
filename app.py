from flask import Flask, request, jsonify
from flask import request
import pandas as pd
import json
from random import randint
from TestAdaptationAlgorithm import adaptAlgo

app = Flask(__name__, static_url_path='', static_folder='frontend/build')

data = pd.read_csv("NumberSenseQuestions.csv")

info = {
    "number": "num 1",
    "question": " "
}


# randomly generate numbers for variables
def random_num(question):
    if "X" in question and "Y" in question:
        x_num = randint(1, 10)
        y_num = randint(1, 10)
        new_ques = question.replace("X", str(x_num))
        new_ques = new_ques.replace("Y", str(y_num))
        return new_ques
    elif "X" in question:
        x_num = randint(1, 10)
        new_ques = question.replace("X", str(x_num))
        return new_ques
    elif "Y" in question:
        y_num = randint(1, 10)
        new_ques = question.replace("Y", str(y_num))
        return new_ques
    else:
        new_ques = question
        return new_ques


# send the frontend the number of questions
@app.route('/num')
def num():
    return {'result': len(data)}


# get first question separate since we always start
# at topic 1, medium level
# use index 1 of D1 for now
@app.route('/questionOne')
def questionOne():
    ques = data.QuestionFormat[1]
    ques_num = data.QuestionID[1]
    user_ques = random_num(ques)
    info["question"] = user_ques
    info["number"] = ques_num
    return info


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    frontInfo = json.loads(request.data)
    newInfo = evaluate(frontInfo['answer'], frontInfo['question'])

    return {'answer': frontInfo["answer"], 'question': str(newInfo['question']), 'number': str(newInfo['num'])}


@app.route('/question', methods=['GET', 'POST'])
def question():
    return {'result': info['question']}


adapt = adaptAlgo()


def evaluate(user_answer, user_ques):
    user_correct = str(eval(str(user_ques))) == user_answer

    # print("----EVAL----")
    # print("USER Q: " + user_ques + " || USER ANS: " + user_answer + " || EXP ANS: " + str(eval(str(user_ques))))
    # print(user_correct)

    index = adapt.getNextQuestion(user_correct)
    newQuestion = random_num(data.QuestionFormat[index])
    newInfo = {'question': newQuestion, 'num': data.QuestionID[index]}
    return newInfo


if __name__ == '__main__':
    app.run(debug=True)