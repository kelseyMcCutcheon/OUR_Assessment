import React from 'react';
import {useState, useEffect} from 'react';
import $ from 'jquery';
import './NumberSense.css';


function NumberSense(){
    const [question, setQuestion] = useState('Question Error');

  useEffect(() => {
    fetch('/numberSense').then(res => res.json()).then(data => {
      setQuestion(data.result);
    });
    }, []);

    return(
        <div className="Test">
            <div>
                {question}
            </div>
        </div>
    )
}

export default NumberSense;
