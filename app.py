from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import request
import pandas as pd
import json

app = Flask(__name__)
CORS(app)


data = pd.read_csv("NumberSenseQuestions.csv")

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


@app.route('/tempquery', methods=['GET', 'POST'])
def tempQuery():

    info = request.json

    unit = info["unit"]
    answer = info["answer"]
    numRight = info["numRight"]
    numWrong = info["numWrong"]

    print("Unit: " + unit + " || ANS: " + answer + " || W: " + str(numWrong) + " || R:" + str(numRight))

    return jsonify("this is TEMPORARY")

@app.route('/getQuestion', methods=['GET', 'POST'])
def getQuestion():
    information = json.loads(request.data)
    print("QINFO")
    print(information)

    qNum = information["QuestionNumber"]

    return jsonify(data.QuestionD1[qNum])





if __name__ == '__main__':
    app.run(debug=True)
