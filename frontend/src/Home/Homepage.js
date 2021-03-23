import { Link } from 'react-router-dom';
import {useState, useEffect} from 'react';
import './Homepage.css';
import {Button} from "react-bootstrap";


function Homepage(){
  const [placeholder, setPlaceholder] = useState('Hi');

  useEffect(() => { from
    fetch('/hello').then(res => res.json()).then(data => {
      setPlaceholder(data.result);
    });
  }, []);

    return(
        <div className="Home">
            <h1>HOMEPAGE</h1>
            {placeholder}
            <Link to='/testSelect'>
                <Button class="btn btn-primary" type="submit">Select</Button>
            </Link>
        </div>
    )
}

export default Homepage;