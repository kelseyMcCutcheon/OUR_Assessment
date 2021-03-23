import React from 'react';
import $ from 'jquery';
import './NumberSense.css';


function NumberSense(){
    let count = 0;

    function ques_count(){
        $.ajax({
            type : "POST",
            url : '/question',
            dataType: "json",
            data: JSON.stringify(count),
            contentType: 'application/json;charset=UTF-8',
            success: function (data) {
                console.log(data);
                }
            });
        count++;
    }

    return(
        <div className="Test">
            <div>
                {ques_count()}
            </div>
            <div className="form">
                <form action="http://localhost:5000/check" method="get">
                    Answer: <input type="text" name="answer"/>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        </div>
    )
}

export default NumberSense;
