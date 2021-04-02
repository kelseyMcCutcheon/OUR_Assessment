from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import request
import pandas as pd
from random import randint

app = Flask(__name__)
CORS(app)


data = pd.read_csv("NumberSenseQuestions.csv")

# iterate through csv questions
# for now just implements random
# num generator in all questions
def iterate_questions():
    ques_list = []
    for x in data.QuestionFormat:
        ques_list.append(random_num(x))

    print(ques_list)
    return ques_list


# randomly generate numbers for variables
def random_num(question):
    if "X" in question and "Y" in question:
        x_num = randint(1,10)
        y_num = randint(1,10)
        new_ques = question.replace("X", str(x_num))
        new_ques = new_ques.replace("Y", str(y_num))
        return new_ques
    elif "X" in question:
        x_num = randint(1,10)
        new_ques = question.replace("X", str(x_num))
        return new_ques
    elif "Y" in question:
        y_num = randint(1,10)
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
@app.route('/question1')
def question1():
    question1 = data.QuestionD1[1]
    return {'result': question1}


# request answer of previous question,
# evaulate in sep function, return next question
@app.route('/nextQuestion', methods=['GET', 'POST'])
def nextQuestion():
    user_answer = request.form.get("user_answer")
    if request.method == 'POST':
        return evaluate(user_answer)
    elif request.method == "GET":
        return evaluate(user_answer)
    else:
        return "Request Error"


# TEST ADAPTATION ALGORITHM
def test_adapt_alg(user_answer):
    pass


def evaluate(user_answer):
    correct = eval(data.QuestionD1[1]) # will have to be changed when change to random num generator
    if str(correct) == user_answer:
        return {'result': 'True'}
    else:
        return {'result': 'False'}



'''
# ask frontend for 5 answers, does not evaluate those answers yet
@app.route('/answers', methods=['GET', 'POST'])
def answers():
    answer1 = request.form.get("answer1")
    answer2 = request.form.get("answer2")
    answer3 = request.form.get("answer3")
    answer4 = request.form.get("answer4")
    answer5 = request.form.get("answer5")
    answer6 = request.form.get("answer6")
    if request.method == 'POST':
        return {'answer1': answer1,
                'answer2': answer2,
                'answer3': answer3,
                'answer4': answer4,
                'answer5': answer5,
                'answer6': answer6}
    else:
        return "Request Error"
'''

if __name__ == '__main__':
    app.run(debug=True)
