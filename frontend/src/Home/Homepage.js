
import { Link } from 'react-router-dom';
import {useState, useEffect} from 'react';
import './Homepage.css';
import {Button} from "react-bootstrap";


function Homepage(){

    return(
        <div className="Home">
            <h1>HOMEPAGE</h1>
            <Link to='/testSelect'>
                <Button className="btn btn-primary" type="submit">Select</Button>
            </Link>
        </div>
    )
}

export default Homepage;