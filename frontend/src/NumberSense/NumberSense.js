import React from 'react';
import {useState, useEffect} from 'react';
import './NumberSense.css';


function NumberSense(){

    const [num, setNum] = useState('Question Number Error')
    useEffect(() => {
        fetch('/question').then(res => res.json()).then(data => {
          setNum(data.number);
        });
    }, []);

    const [ques, setQues] = useState("Question Error");
    useEffect(() => {
        fetch('/question').then(res => res.json()).then(data => {
          setQues(data.question);
        });
    }, []);


    const [nextQuestion, setNextQuestion] = useState('Next Question Error');
    useEffect(() => {
        fetch('/nextQuestion').then(res => res.json()).then(data => {
          setNextQuestion(data.result);
        });
    }, []);

    useEffect(() => {
    fetch('/num').then(res => res.json()).then(data => {
      setQuesNum(data.result);
    });
    }, []);

    var user_ques = ques

    return(
        <html>
            <div className="Test">
                <p>
                    <form action="/nextQuestion" method="POST">
                        {num}  {ques}: <input type="text" name="user_answer" ></input><br></br>
                        <input type="submit" value="Submit" name="count"></input>
                    </form>
                </p>
            </div>
        </html>
    )
}
export default NumberSense;
