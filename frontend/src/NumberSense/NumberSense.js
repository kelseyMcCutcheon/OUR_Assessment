import React, { Component } from 'react';
import {useState, useEffect} from 'react';
import { readString } from 'papaparse';
import $ from 'jquery';
import './NumberSense.css';
import axios from 'axios';


function NumberSense(){
    const [question, setQuestion] = useState('Question Error');

  useEffect(() => {
    fetch('/numberSense').then(res => res.json()).then(data => {
      setQuestion(data.result);
    });
    }, []);

    return(
        <html>
            <div className="Test">
                {question}
              <form onSubmit={fetchData} method = "post">
                 Answer:<input type ="text" name="ans" />
                 <input type="submit" value = "submit" />
              </form>
            </div>
        </html>
    )
}
export default NumberSense;
