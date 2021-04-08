import React from 'react';
import {useState, useEffect} from 'react';
import './NumberSense.css';
import $ from 'jquery';

function NumberSense(){

    const [num, setNum] = useState('Question Number Error')
    const [ques1, setQues1] = useState("Question 1 Error");
    useEffect(() => {
        fetch('/questionOne').then(res => res.json()).then(data => {
          setNum(data.number);
          setQues1(data.question);
        });
    }, []);

    const [tempQuestion, setTempQuestion] = useState(ques1);
        useEffect(() => {
        fetch('/question').then(res => res.json()).then(data => {
          setTempQuestion(data.result);
        });
    }, []);

    const [answer, setAnswer] = useState(" ");
    const submit = (e) => {
        const info = {'number': num, 'answer': answer, 'question': ques1};

        e.preventDefault()
        fetch('/answer', {
            method: 'POST',
            body: JSON.stringify(info),
            headers: {'Content-Type': 'application/json' },
        })
        .then(res => res.json())
        .then(data => {
            setAnswer(data.answer)
            setTempQuestion(data.question)
        })
    }

    return(
    <div className="Test">

    <form onSubmit={submit}>
          {num}  {tempQuestion}: <input
                            type="text"
                            name="answer"
                            value={answer}
                            onChange = {e => setAnswer(e.target.value)}
                            />
          <input type="submit" value="Submit" name="count"></input>
      </form>
        {answer}<br></br>
    </div>
    )
}
export default NumberSense;
