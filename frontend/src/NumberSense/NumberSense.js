import React from 'react';
import {useState, useEffect} from 'react';
import './NumberSense.css';


function NumberSense(){
    const [quesNum, setQuesNum] = useState(0);

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

    /*
    const [answer1, setAnswer1] = useState('No Answer');
    const [answer2, setAnswer2] = useState('No Answer');
    const [answer3, setAnswer3] = useState('No Answer');
    const [answer4, setAnswer4] = useState('No Answer');
    const [answer5, setAnswer5] = useState('No Answer');

    useEffect(() => {
        fetch('/answers').then(res => res.json()).then(data => {
      setAnswer1(data.question1);
      setAnswer2(data.question2);
      setAnswer3(data.question3);
      setAnswer4(data.question4);
      setAnswer5(data.question5);
    });
    }, []);

        */


    return(
        <html>
            <div className="Test">
                <p>
                    {question}<br></br>
                    {question[1]}
                </p>
            </div>
        </html>
    )
}
export default NumberSense;
