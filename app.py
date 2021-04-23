from flask import Flask, request, jsonify, render_template, redirect, url_for
import pandas as pd
import json
from random import randint
from TestAdaptationAlgorithm import adaptAlgo

app = Flask(__name__)

data = pd.read_csv("NumberSenseQuestions.csv")

test = []

info = {
    "number": "num 1",
    "question": " ",
}

backEndInfo = {
    "question_id": "",
    "question_index": 1,
    "question": "",
    "question_for_human": "",
    "answer": "",
    "user_answer": ""
}

variables = {
    "X": 0,
    "Y": 0,
    "Z": 0,
    "W": 0
}

'''
@app.route('/')
def index():
    return render_template('index.html')
'''


def replaceForHuman(forHuman, question) -> str:
    if "XX" in forHuman:
        return forHuman.replace("XX", question)
    else:
        print("MARKER NOT FOUND: " + forHuman)
        return question


# randomly generate numbers for variables
def newVariables(rangeMin=1, rangeMax=9) -> dict:
    for x in variables:
        newInt = randint(rangeMin, rangeMax)
        if newInt == variables[x]:
            while newInt == variables[x]:
                newInt = randint(rangeMin, rangeMax)
        variables[x] = newInt
    # print(variables)
    return variables


def evalString(question) -> str:
    result = ""
    parts = question.split(";")
    for x in parts:
        tmp = x
        if "$" in x:
            tmp = tmp.replace("$", "")
            tmp = str(eval(tmp))
        result += tmp
    return result


def replaceVariables(question) -> str:
    for x in variables:
        if x in question:
            question = question.replace(x, str(variables[x]))
    return question


def evaluateAnswer(correctAnswer, userAnswer) -> bool:
    if userAnswer == correctAnswer:
        print("CORRECT!")
        unit = backEndInfo['question'].split('.')
        test.append({'number': backEndInfo['question_id'], 'question': backEndInfo['question'], 'userResult': 'Correct',
                     'unit': unit})
        return True
    else:
        print("INCORRECT.")
        test.append({'number': backEndInfo['question_id'], 'userResult': 'Incorrect'})
        return False


def evaluateQuestionAnswer(answer, type) -> str:
    if type == "math":
        return eval(answer)
    elif type == "stringEval":
        return evalString(answer)
    else:
        return "UNKNOWN TYPE"


def setUpNewQuestion(index):
    newVariables()

    # we have a new question
    question = data.QuestionFormat[index]
    question = replaceVariables(question)
    backEndInfo["question"] = question

    # we have a new answer
    type = data.QuestionType[index]
    answer = data.Answer[index]
    answer = replaceVariables(answer)
    answer = evaluateQuestionAnswer(answer, type)
    backEndInfo["answer"] = str(answer)

    forHuman = data.QuestionForHuman[index]
    forHuman = replaceForHuman(forHuman, question)

    backEndInfo["question_id"] = data.QuestionID[index]
    backEndInfo["question_for_human"] = forHuman


# send the frontend the number of questions
@app.route('/num')
def num():
    return {'result': len(data)}


# get first question separate since we always start
# at topic 1, medium level
# use index 1 of D1 for now
@app.route('/questionOne')
def questionOne():
    if backEndInfo["question_for_human"] == "":
        setUpNewQuestion(1)

    info["question"] = backEndInfo["question_for_human"]
    info["number"] = backEndInfo["question_id"]
    return info


@app.route('/answer', methods=['GET', 'POST'])
def answer():
    frontInfo = json.loads(request.data)
    newInfo = evaluate(frontInfo['answer'])
    if newInfo == 'END':
        return {'end': 'END'}
    else:
        return {'answer': frontInfo["answer"], 'question': str(newInfo['question']), 'number': str(newInfo['num'])}


@app.route('/question', methods=['GET', 'POST'])
def question():
    return {'result': backEndInfo["question_for_human"]}


def check_input(ans):
    try:
        ans = eval(ans)
    except (SyntaxError, ValueError, NameError):
        print("could not eval")
    return ans


adapt = adaptAlgo()


def evaluate(user_answer):
    correct_answer = backEndInfo["answer"]
    # do not try to evaluate % sign
    user_answer = str(user_answer)
    if '%' in user_answer:
        user_answer = user_answer[:-1]
    user_answer = check_input(user_answer)

    if '.' in correct_answer:
        if correct_answer.split('.')[1] == '0':
            correct_answer = round(float(correct_answer))
        elif '.' in correct_answer:
            correct_answer = round(float(correct_answer), 2)

    user_correct = evaluateAnswer(str(correct_answer), str(user_answer))

    index = adapt.getNextQuestion(user_correct)
    # if index is within available data, set up new question
    if index <= len(data):
        setUpNewQuestion(index)

        newInfo = {'question': backEndInfo["question_for_human"], 'num': data.QuestionID[index]}
        return newInfo
    # if index is out of data range, end test
    else:
        return 'END'


# send test info for graphing
@app.route('/test_info', methods=['GET', 'POST'])
def test_info():
    units = []
    # hardcoded unit values for now
    u1_questions_correct = 0
    u1_questions_incorrect = 0
    u2_questions_correct = 0
    u2_questions_incorrect = 0
    u4_questions_correct = 0
    u4_questions_incorrect = 0
    for t in test:
        unit = t['number'].split('.')[0]
        if unit not in units:
            units.append(unit)
    for t in test:
        if t['number'].split('.')[0] == str(1):
            if t['userResult'] == 'Correct':
                u1_questions_correct += 1
            else:
                u1_questions_incorrect += 1
        elif t['number'].split('.')[0] == str(2):
            if t['userResult'] == 'Correct':
                u2_questions_correct += 1
            else:
                u2_questions_incorrect += 1
        elif t['number'].split('.')[0] == str(4):
            if t['userResult'] == 'Correct':
                u4_questions_correct += 1
            else:
                u4_questions_incorrect += 1

    unit_parsed_data = [
        {"unit": "Unit 1", "numberCorrect": u1_questions_correct, "numberIncorrect": u1_questions_incorrect},
        {"unit": "Unit 2", "numberCorrect": u2_questions_correct, "numberIncorrect": u2_questions_incorrect},
        {"unit": "Unit 4", "numberCorrect": u4_questions_correct, "numberIncorrect": u4_questions_incorrect}]

    return jsonify(result=unit_parsed_data)


if __name__ == '__main__':
    app.run(debug=True)
