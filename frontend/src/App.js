import react from 'react';
import {Route, Switch, BrowserRouter as Router} from "react-router-dom";
import Select from "./Select/Select";
import NumberSense from "./NumberSense/NumberSense";

import './OurAssessment.css';

import Homepage from "./Home/Homepage";
import AboutPage from "./AboutPage/About";

function App() {
  return (
    <div className='OurAssessmentApp'>
      <header><h1 className='AppHeader'>Our Assessment</h1></header>
      <Router>
          <Switch>
              <Route exact path="/" component={Homepage} />
              <Route path='/testSelect' component={Select} />
              <Route path='/aboutpage' component={AboutPage} />
              <Route path='/numberSense' component={NumberSense} />
          </Switch>
      </Router>
    </div>
  );
}

export default App;