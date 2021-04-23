
import { Link } from 'react-router-dom';
import './Homepage.css';
import {Button} from "react-bootstrap";


function Homepage(){

    return(
        <div className="Home">
            <header id='Title'>
                <h1>Welcome!</h1>
            </header>
            <Link to='/testSelect'>
                <Button className="btn btn-primary HomepageButton" type="submit">Start (Y)OUR Assessment</Button>
            </Link>
            <br/>
            <Link to='/aboutpage'>
                <Button className="btn btn-primary HomepageButton" type="submit">About OUR Assessment</Button>
            </Link>
        </div>
    )
}

export default Homepage;