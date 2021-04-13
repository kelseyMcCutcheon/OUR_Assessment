from flask import Flask, request, jsonify, render_template, send_from_directory, make_response
import pandas as pd
import json
from random import randint
from TestAdaptationAlgorithm import adaptAlgo

app = Flask(__name__)

data = pd.read_csv("NumberSenseQuestions.csv")

info = {
    "number": "num 1",
    "question": " ",
}

backEndInfo = {
    "question_id" : "",
    "question_index" : 1,
    "question" : "",
    "question_for_human": "",
    "answer" : "",
    "user_answer" : ""
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
        return True
    else:
        print("INCORRECT.")
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
    user_answer = check_input(user_answer)

    #correct_answer = round(int(correct_answer))
    print("correct:" + str(correct_answer))
    print("user:" + str(user_answer))

    user_correct = evaluateAnswer(str(correct_answer), str(user_answer))

    index = adapt.getNextQuestion(user_correct)
    # if index is within available data, set up new question
    if index <= 35:
        setUpNewQuestion(index)

        newInfo = {'question': backEndInfo["question_for_human"], 'num': data.QuestionID[index]}
        return newInfo
    # if index is out of data range, end test
    else:
        end_test()


def end_test():
    print("END OF TEST")


if __name__ == '__main__':
    app.run(debug=True)
