from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import request
import pandas as pd

app = Flask(__name__)
CORS(app)


def number_sense_test():
    data = pd.read_csv("NumberSenseQuestions.csv")
    ques_and_ans = []
    for question in data.QuestionD1:
        ques_dict = {
            "question": question,
            "answer": answer
        }
        ques_and_ans.append(ques_dict)
    return ques_and_ans


def answer(question):
    correct = eval(question)
    user_answer = request.args.get('user_answer')
    if user_answer == correct:
        return "Correct!"
    else:
        return "Incorrect!"


@app.route('/numberSense')
def number_sense():
    return {'result': number_sense_test()}


if __name__ == '__main__':
    app.run(debug=True)
