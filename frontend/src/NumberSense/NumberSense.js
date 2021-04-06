import React from 'react';
import {useState, useEffect} from 'react';
import './NumberSense.css';
import $ from 'jquery';

function NumberSense(){

    const [CurrentQuestionNum, setCurrentQuestion] = useState(1);

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

    const submit = (e) => {
        console.log(tempAnswer);
        e.preventDefault()
        fetch('/tempquery', {
            method: 'POST',
            body: JSON.stringify(tempAnswer),
            headers: {'Content-Type': 'application/json' },
        })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
    }


    const [tempAnswer, setTempAnswer] = useState("");
    const [tempQuestion, setTempQuestion] = useState("");
    useEffect(() => {

        const info = {
            "QuestionNumber": CurrentQuestionNum
        };

        fetch('/getQuestion', {
            method: 'POST',
            body: JSON.stringify(info),
        })
        .then(res => res.json()).then(data => {
            setTempQuestion(data);
        });
        });

    return(
    <div className="Test">

    <form onSubmit={submit}>
          {num}  {ques}: <input
                            type="text"
                            name="answer"
                            value={tempAnswer}
                            onChange = {e => setTempAnswer(e.target.value)}
                            />
          <input type="submit" value="Submit" name="count"></input>
      </form>
    </div>
    )
}
export default NumberSense;
