import {Link} from "react-router-dom";
import {Button} from "react-bootstrap";
import "./Select.css"

function Select(){
    return(
        <div className="Select">
            <Link to="/">
                <button id='backButton'>Back</button>
            </Link>
            <h1>Select A Course</h1>
            <Link to ='/numberSense'>
                <Button className="SelectButton" id="numberSenseButton">Number Sense</Button>
            </Link>
        </div>
    )
}

export default Select;