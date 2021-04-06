from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import request
import pandas as pd
import json
from random import randint
from TestAdaptationAlgorithm import adaptAlgo


app = Flask(__name__)
CORS(app)

data = pd.read_csv("NumberSenseQuestions.csv")

EASY_WRONG = 3
EASY_RIGHT = 2
MED_WRONG = 2
MED_RIGHT = 2
HARD_WRONG = 2
HARD_LIMIT = 3

info = {
    "number": "num 1",
    "question": " ",
    "correct_count": 0,
    "incorrect_count": 0
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
@app.route('/question')
def question():
    ques = data.QuestionFormat[1]
    ques_num = data.QuestionID[1]
    user_ques = random_num(ques)
    info["question"] = user_ques
    info["number"] = ques_num
    return info


@app.route('/tempquery', methods=['GET', 'POST'])
def tempQuery():

    info = json.loads(request.json)
    print(info)
    #unit = info["unit"]
    #answer = info["answer"]

   # print("ANS: " + answer)

    return jsonify("this is TEMPORARY")


@app.route('/getQuestion', methods=['GET', 'POST'])
def getQuestion():
    information = json.loads(request.data)
    print("QINFO")
    print(information)

    qNum = information["QuestionNumber"]

    return jsonify(data.QuestionD1[qNum])


# request answer of previous question,
# evaluate in sep function, return next question
@app.route('/nextQuestion', methods=['GET', 'POST'])
def nextQuestion():
    user_answer = request.form.get("user_answer")
    user_ques = info["question"]
    if request.method == 'POST':
        return evaluate(user_answer, user_ques)
    elif request.method == "GET":
        return evaluate(user_answer, user_ques)
    else:
        return "Request Error"


def evaluate(user_answer, user_ques):
    correct = eval(str(user_ques)) == user_answer
    nextQuestionIndex = data.QuestionFormat[adaptAlgo.getnextQuestion(correct)]
    info["question"] = nextQuestionIndex
    return info


if __name__ == '__main__':
    app.run(debug=True)
