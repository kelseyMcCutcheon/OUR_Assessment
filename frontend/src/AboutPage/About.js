//import react from 'react';
import './About.css';
import {Link} from 'react-router-dom';

function AboutPage() {
    return(
        <div className='AboutPage'>

                <Link to="/">
                    <button className='AboutBackButton'>Back</button>
                </Link>

            <h1 className='AboutHeader'>About Our Assessment</h1>
            <p className='AboutText'>
                Our Assessment was made by Adam, Kelsey, Sawyer.
            </p>
        </div>
    );
}

export default AboutPage;