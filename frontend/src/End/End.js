import React from 'react';
import {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';
import Paper from '@material-ui/core/Paper';
import {
  Chart,
  BarSeries,
  Title,
  ArgumentAxis,
  ValueAxis,
} from '@devexpress/dx-react-chart-material-ui';
import {Animation } from '@devexpress/dx-react-chart';


const data = [
  { year: '1950', population: 2.525 },
  { year: '1960', population: 3.018 },
  { year: '1970', population: 3.682 },
  { year: '1980', population: 4.440 },
  { year: '1990', population: 5.310 },
  { year: '2000', population: 6.127 },
  { year: '2010', population: 6.930 },
];


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
                <ArgumentAxis/>
                <ValueAxis max={7}/>

                <BarSeries
                    valueField="numberQuestion"
                    argumentField="unit"
                />
                <Title text="Test Data"/>
                <Animation/>
              </Chart>
            </Paper>
            {testInfo.map(t => <div>{t.unit}</div>)}
          </div>
      );
  }

export default End;