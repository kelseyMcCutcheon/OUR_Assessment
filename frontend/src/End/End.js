import React from 'react';
import {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import Paper from '@material-ui/core/Paper';
import {
  Chart,
  ArgumentAxis,
  ValueAxis,
  BarSeries,
  Title,
  Legend,
} from '@devexpress/dx-react-chart-material-ui';
import { withStyles } from '@material-ui/core/styles';
import {Stack, Animation } from '@devexpress/dx-react-chart';


function End(){

  const [testInfo, setTestInfo] = useState([]);
    useEffect(() => {
        fetch('/test_info').then(res => res.json()).then(data => {
          setTestInfo(data.result);
        });
    }, []);

    const chartData=testInfo;
      return (
          <div className="App">
            <Paper>
              <Chart
                  data={chartData}
              >
                <ArgumentAxis />
                <ValueAxis max={7}/>

                <BarSeries
                    name = "Correct Answers"
                    valueField="numberCorrect"
                    argumentField="unit"
                />
                <BarSeries
                    name = "Incorrect Answers"
                    valueField="numberIncorrect"
                    argumentField="unit"
                />
                <Animation/>
                <Title text="Test Data" />
                <Stack
                  stacks={[
                    { series: ['Correct Answers', 'Incorrect Answers'] },
                  ]}
                />
              </Chart>
            </Paper>
          </div>
      );
  }

export default End;