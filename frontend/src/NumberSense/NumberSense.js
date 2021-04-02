import React from 'react';
import {useState, useEffect} from 'react';
import './NumberSense.css';


function NumberSense(){
    const [quesNum, setQuesNum] = useState(0);
    const [info, setInfo] = useState({'answer': ""});

    useEffect(() => {
    fetch('/num').then(res => res.json()).then(data => {
      setQuesNum(data.result);
    });
    }, []);

    const [question, setQuestion] = useState('Question Error');
    useEffect(() => {
        fetch('/questions').then(res => res.json()).then(data => {
          setQuestion(data);
        });
    }, []);

    const submit = (e) => {
        console.log(info);
        e.preventDefault()
        fetch('/tempquery', {
            method: 'POST',
            body: JSON.stringify({info}),
            headers: {'Content-Type': 'application/json' },
        })
        .then(res => res.json())
        .then(data => {console.log(data)})
    }

    const changeHandler = (e) => {
        setInfo({...info, "answer": e.target.value})
    }

    return(
        <div className="Test">
                <p>
                    {question}<br></br>
                    {question[1]}
                </p>
                <form onSubmit={submit}>
                        {question[1]}: 
                        <input 
                            type="text" 
                            name="answer"
                            value={info["answer"]}
                            onChange = {changeHandler}
                            />
                            <br/>
                        <input type="submit" value="Submit"></input>
                </form>
        </div>
    )
}
export default NumberSense;
