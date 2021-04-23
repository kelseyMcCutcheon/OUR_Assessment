  
import React from 'react';
import {useState, useEffect} from 'react';
import './NumberSense.css';
import { Link } from 'react-router-dom';
//import $ from 'jquery';

function NumberSense(){

    const [num, setNum] = useState('Question Number Error')
    const [ques1, setQues1] = useState("Question 1 Error");
    useEffect(() => {
        fetch('/questionOne').then(res => res.json()).then(data => {
          setNum(data.number);
          setQues1(data.question);
        });
    }, []);

    const [question, setQuestion] = useState(ques1);
        useEffect(() => {
        fetch('/question').then(res => res.json()).then(data => {
          setQuestion(data.result);
        });
    }, []);

    const [answer, setAnswer] = useState("");
    const [isEnd, setIsEnd] = useState("");

    const submit = (e) => {
        const info = {'number': num, 'answer': answer, 'question': question};
        document.getElementById("Form").reset()
        e.preventDefault()
        fetch('/answer', {
            method: 'POST',
            body: JSON.stringify(info),
            headers: {'Content-Type': 'application/json' },
        })
        .then(res => res.json())
        .then(data => {
            setAnswer("");
            setQuestion(data.question);
            setNum(data.number);
            setIsEnd(data.end);
            if(data.end == "END"){
                document.getElementById("Form").style.display = "none";
                document.getElementById("question").style.display = "none";
                document.getElementById("questionID").style.display = "none";
            }
        });

    }

    return(
    <div className="Test">
        <Link to="/">
                <button id='backButton'>Quit to Homepage</button>
        </Link>

        <div id="questionID">Question: {num}</div>
        <div id="question">{question}</div>
        <br/>
        <form onSubmit={submit} id="Form" autoComplete="off">
            <input id="form_input" type="text" name="answer" value={answer} onChange = {e => setAnswer(e.target.value)}/>
            <br/>
            <input id="form_button" type="submit" value="Submit" name="count"></input>
        </form>
        <h1><Link to='/end'>{isEnd}</Link></h1>
    </div>
    )
}
export default NumberSense;