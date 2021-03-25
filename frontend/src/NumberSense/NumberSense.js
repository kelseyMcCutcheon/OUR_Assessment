import React from 'react';
import {useState, useEffect} from 'react';
import $ from 'jquery';
import './NumberSense.css';
import axios from 'axios';
import '.././'


function NumberSense(){
    const [count, setCount] = useState(0);
    const [question, setQuestion] = useState('Question Error');
    const [user, setUser] = useState('NULL')

  useEffect(() => {
    fetch('/numberSense').then(res => res.json()).then(data => {
      setQuestion(data.result);
    });
    }, []);

    useEffect(() => {
    fetch('/check').then(res => res.json()).then(data => {
      setUser(data.result);
    });
    }, []);

    return(
        <html>
            <div className="Test">
                {question}
              <form action="/check" method = "post">
                 Answer:<input type ="text" name="ans" />
                 <input onSubmit={() => setCount(count+1)} type="submit" value = "submit" />
              </form>
                {user}
            </div>
        </html>
    )
}

export default NumberSense;
