from flask import Flask
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)


def number_sense_test():
    data = pd.read_csv("NumberSenseQuestions.csv")
    return data.QuestionD1[1]


@app.route('/numberSense')
def number_sense():
    return {'result': number_sense_test()}
