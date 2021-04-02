from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import request
import pandas as pd

app = Flask(__name__)
CORS(app)


data = pd.read_csv("NumberSenseQuestions.csv")

# iterate through csv questions, return dictionary
# of question num and question
def iterate_questions():
    ques_list = []
    for x in data.QuestionD1:
        ques_list.append(x)
    return ques_list


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


if __name__ == '__main__':
    app.run(debug=True)
