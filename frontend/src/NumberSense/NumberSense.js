import React, { Component } from 'react';
import {useState, useEffect} from 'react';
import { readString } from 'papaparse';
import $ from 'jquery';
import './NumberSense.css';
import axios from 'axios';


function NumberSense(){
    const [question, setQuestion] = useState('Question Error');
    const [question1, setQuestion1] = useState('No Question');
    const [question2, setQuestion2] = useState('No Question');
    const [question3, setQuestion3] = useState('No Question');
    const [question4, setQuestion4] = useState('No Question');
    const [question5, setQuestion5] = useState('No Question');

    const [answer1, setAnswer1] = useState('No Answer');
    const [answer2, setAnswer2] = useState('No Answer');
    const [answer3, setAnswer3] = useState('No Answer');
    const [answer4, setAnswer4] = useState('No Answer');
    const [answer5, setAnswer5] = useState('No Answer');

    /*
  useEffect(() => {
    fetch('/numberSense').then(res => res.json()).then(data => {
      setQuestion(data.result);

    });
    }, []); */

    useEffect(() => {
    fetch('/questions').then(res => res.json()).then(data => {
      setQuestion1(data.question1);
      setQuestion2(data.question2);
      setQuestion3(data.question3);
      setQuestion4(data.question4);
      setQuestion5(data.question5);
    });
    }, []);

    useEffect(() => {
        fetch('/answers').then(res => res.json()).then(data => {
      setAnswer1(data.question1);
    });
    }, []);


    return(
        <html>
            <div className="Test">
                <p>
                    <form action="http://localhost:5000/answers" method="POST">
                        {question1}: <input type="text" name="answer1" ></input><br></br>
                        {question2}: <input type="text" name="answer2" ></input><br></br>
                        {question3}: <input type="text" name="answer3" ></input><br></br>
                        {question4}: <input type="text" name="answer4" ></input><br></br>
                        {question5}: <input type="text" name="answer5" ></input><br></br>
                        <input type="submit" value="Submit"></input>
                    </form>
                </p>
            </div>
        </html>
    )
}
export default NumberSense;
