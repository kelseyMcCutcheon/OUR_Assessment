import React from 'react';
import {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';


function End(){
    const [test, setTest] = useState([]);


    useEffect(() => {
        fetch('/test_info').then(res => res.json()).then(data => {
            setTest(data.result)
        });
    }, []);


  return (
    <div className="App">
      <html>
        <head>
        <script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
        <script type="text/javascript">

        window.onload = function () {
            var chart = new CanvasJS.Chart("chartContainer", {
                title:{
                    text: "My First Chart in CanvasJS"
                },
                data: [
                {
                    // Change type to "doughnut", "line", "splineArea", etc.
                    type: "column",
                    dataPoints: [
                        { label: "apple",  y: 10  },
                        { label: "orange", y: 15  },
                        { label: "banana", y: 25  },
                        { label: "mango",  y: 30  },
                        { label: "grape",  y: 28  }
                    ]
                }
                ]
            });
            chart.render();
        }
        </script>
        </head>
        <body>
        <div id="chartContainer" style="height: 300px; width: 100%;"></div>
        </body>
        </html>
    </div>
  )


}

export default End;