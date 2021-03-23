import {Link} from "react-router-dom";
import {Button} from "react-bootstrap";
import "./Select.css"

function Select(){
    return(
        <div className="Select">
            <h1>Select A Course</h1>
            <Link to ='/numberSense'>
                <Button>Number Sense</Button>
            </Link>
        </div>
    )
}

export default Select;