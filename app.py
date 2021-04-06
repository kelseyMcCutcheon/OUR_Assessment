from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import request
import pandas as pd
from random import randint


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


def adaptAlgo(correct, questionNumber, numWrong, numRight):
    section = questionNumber.split('.')[1]
    difficulty = questionNumber.split('.')[2]

    nextQuestion = 0

    if (correct):
        if difficulty == 0:
            if numRight >= EASY_RIGHT:
                difficulty = 1
        elif difficulty == 1:
            if numRight >= MED_RIGHT:
                difficulty = 2
        else:
            if numRight + numWrong >= HARD_LIMIT:
                # print("Moving on to the next section!")
                section += 1
                difficulty = 1
    else:
        if difficulty == 0:
            if numWrong >= EASY_WRONG:
                # print("Moving on to the next section!")
                section += 1
                difficulty = 1
        elif difficulty == 1:
            if numWrong >= MED_WRONG:
                difficulty = 0
        else:
            if numWrong + numRight >= HARD_LIMIT:
                # print("Moving on to the next section!")
                section += 1
                difficulty = 1
            elif numWrong >= HARD_WRONG:
                difficulty = 2

    nextQuestion = (section * 3) + difficulty
    return nextQuestion


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
    correct = eval(str(user_ques))
    adaptAlgo(correct, info["number"], info["incorrect_count"], info["correct_count"])


if __name__ == '__main__':
    app.run(debug=True)
