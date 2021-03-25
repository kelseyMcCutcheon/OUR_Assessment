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


# allow both GET and POST requests
@app.route('/test', methods=['GET', 'POST'])
def test():
    data = pd.read_csv("NumberSenseQuestions.csv")
    question1 = data.QuestionD1[1]
    question2 = data.QuestionD1[2]
    question3 = data.QuestionD1[3]
    question4 = data.QuestionD1[4]
    question5 = data.QuestionD1[5]
    """
    answer1 = request.form.get('answer1')
    answer2 = request.form.get('answer2')
    answer3 = request.form.get('answer3')
    answer4 = request.form.get('answer3')
    answer5 = request.form.get('answer3')"""

    # handle the POST request
    if request.method == 'POST':
        return '''
                  <h2>Correct Answer is: {}</h2>
                  <h2>Correct Answer is: {}</h2>
                  <h2>Correct Answer is: {}</h2>
                  <h2>Correct Answer is: {}</h2>
                  <h2>Correct Answer is: {}</h2>
                  '''.format(eval(question1), eval(question2), eval(question3), eval(question4), eval(question5))

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>{}: <input type="text" name="answer1"></label></div>
               <div><label>{}: <input type="text" name="answer2"></label></div>
               <div><label>{}: <input type="text" name="answer3"></label></div>
               <div><label>{}: <input type="text" name="answer4"></label></div>
               <div><label>{}: <input type="text" name="answer5"></label></div>
               <input type="submit" value="Submit">
           </form>'''.format(question1, question2, question3, question4, question5)


@app.route('/numberSense')
def number_sense():
    return {'result': number_sense_test()}


if __name__ == '__main__':
    app.run(debug=True)
