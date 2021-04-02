import React from 'react';
import {useState, useEffect} from 'react';
import './NumberSense.css';


function NumberSense(){
    
    //const [quesNum, setQuesNum] = useState(0);
    const [CurrentQuestionNum, setCurrentQuestion] = useState(1);

    const [numQWrong, setNumQWrong] = useState(0);
    const [numQRight, setNumQRight] = useState(0);

    // useEffect(() => {
    // fetch('/num').then(res => res.json()).then(data => {
    //   setQuesNum(data.result);
    // });
    // }, []);

    // const [question, setQuestion] = useState('Question Error');
    // useEffect(() => {
    //     fetch('/questions').then(res => res.json()).then(data => {
    //       setQuestion(data);
    //     });
    // }, []);

    

    const submit = (e) => {

        //Setting up query to flask
        const info = {
            "unit": "numberSense",
            "answer": tempAnswer,
            "currentQuestion": CurrentQuestionNum,
            "numWrong": numQWrong,
            "numRight": numQRight
        };

        console.log(info);
        e.preventDefault()
        fetch('/tempquery', {
            method: 'POST',
            body: JSON.stringify(info),
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
    

    //{question}
    //<br/>
    //{question[1]}

    return(
        <div className="Test">
                <p>
                    {tempQuestion}
                </p>
                <form onSubmit={submit}> 
                        <input 
                            type="text" 
                            name="answer"
                            value={tempAnswer}
                            onChange = {e => setTempAnswer(e.target.value)}
                            />
                            <br/>
                        <input type="submit" value="Submit"></input>
                </form>
        </div>
    )
}
export default NumberSense;
