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
        '''
        ques_dict = {
            "question": question,
            "answer": answer(question)
        }
        print(ques_dict)
        ques_and_ans.append(ques_dict)
        '''
        ques_and_ans.append(question)
        user_answer = request.args.get('user_answer')
    return ques_and_ans


def answer(test_ans):
    return test_ans


'''
def answer(test_ans):
    print(test_ans)
    correct = eval(test_ans)
    user_answer = request.args.get('user_answer')
    if user_answer == correct:
        return "Correct!"
    else:
        return "Incorrect!"
'''
data = pd.read_csv("NumberSenseQuestions.csv")


# iterate through csv questions, return dictionary
# of question num and question
def iterate_questions():
    ques_list = {}
    num = 1
    for x in data.QuestionD1:
        ques_num = 'question' + str(num)
        num += 1
        ques_list[ques_num] = x
    return ques_list


# get questions from iterating csv
@app.route('/questions')
def questions():
    return iterate_questions()


'''
# send 5 questions to front end
@app.route('/questions', methods=['GET', 'POST'])
def questions():
    question1 = data.QuestionD1[1]
    question2 = data.QuestionD1[2]
    question3 = data.QuestionD1[3]
    question4 = data.QuestionD1[4]
    question5 = data.QuestionD1[5]

    return {'question1': question1,
            'question2': question2,
            'question3': question3,
            'question4': question4,
            'question5': question5}
'''


# ask frontend for 5 answers, does not evaluate those answers yet
@app.route('/answers', methods=['GET', 'POST'])
def answers():
    answer1 = request.form.get("answer1")
    answer2 = request.form.get("answer2")
    answer3 = request.form.get("answer3")
    answer4 = request.form.get("answer4")
    answer5 = request.form.get("answer5")
    if request.method == 'POST':
        return {'answer1': answer1,
                'answer2': answer2,
                'answer3': answer3,
                'answer4': answer4,
                'answer5': answer5}
    else:
        return "Request Error"


if __name__ == '__main__':
    app.run(debug=True)
