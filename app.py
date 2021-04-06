from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import request
import pandas as pd
from random import randint

app = Flask(__name__)
CORS(app)

data = pd.read_csv("NumberSenseQuestions.csv")

info = {
    "number": "num 1",
    "question": " ",
    "difficulty_index": 1,
    "correct_count": 0,
    "incorrect_count": 0,
    "unit": " ",
    "topic": " "
}


# iterate through csv questions
# for now just implements random
# num generator in all questions
def iterate_questions():
    ques_list = []
    for x in data.QuestionFormat:
        ques_list.append(random_num(x))
    return ques_list


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


# get questions from iterating csv
@app.route('/questions')
def questions():
    return jsonify(iterate_questions())


# get first question separate since we always start
# at topic 1, medium level
# use index 1 of D1 for now
@app.route('/question')
def question():
    ques = data.QuestionFormat[info["difficulty_index"]]
    ques_num = data.QuestionID[info["difficulty_index"]]
    user_ques = random_num(ques)
    info["question"] = user_ques
    info["number"] = ques_num
    info["unit"] = info["number"].split('.')[1]
    info["topic"] = info["number"].split('.')[2]
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


# TEST ADAPTATION ALGORITHM
def test_adapt_alg(user_answer):
    if user_answer:
        info["correct_count"] += 1  # up correct answer count
        # check if correct count is high enough to move up a difficulty level
        # 2 right for now, change?
        if info["correct_count"] == 2:
            info["difficulty_index"] += 1  # up difficulty level by 1
            # reset correct and incorrect counts for new topic
            info["correct_count"] = 0
            info["incorrect_count"] = 0
        return question()
    elif user_answer == "false":
        info["incorrect_count"] -= 1  # up incorrect answer count
        # check if incorrect count is high enough to move down a difficulty level
        # 2 wrong for now, change?
        if info["incorrect_count"] == 2:
            info['difficulty_index'] -= 1  # down a difficulty level by 1
            # reset correct and incorrect counts for new topic
            info["correct_count"] = 0
            info["incorrect_count"] = 0
        # check if student has reached hard limit for questions in topic
        # if yes, move student on to next topic
        # re-evaluate hard limits
        if info["topic_count"] == 10:
            print(info["number"].split('.'))
        return question()
    else:
        return "Evaluation Error"


def evaluate(user_answer, user_ques):
    correct = eval(user_ques)
    if str(correct) == user_answer:
        return test_adapt_alg(True)
    else:
        return test_adapt_alg(False)


if __name__ == '__main__':
    app.run(debug=True)
