//import react from 'react';
import './About.css';
import {Link} from 'react-router-dom';

function AboutPage() {
    return(
        <div className='AboutPage'>

            <Link to="/">
                <button id='backButton'>Back</button>
            </Link>

            <h1 className='AboutHeader'>About Our Assessment</h1>
            <p className='AboutInfo' id="AboutText">
                &emsp;Our Assessment was created by Sawyer Eden Cawley-Edwards, Adam Currier, and Kelsey McCutcheon.
                The purpose of this capstone project is to create a competency-based mathematics placement test, 
                the focus of which is to provide students with an unbiased assessment of their actual mathematics skills. 
                With This assessment we hope to determine whether or not a student is considered ‘competent’ in a certain mathematical level. 
                As well as give students useful and personalized information about what specific concepts they need to focus their efforts on.
            </p>
        </div>
    );
}

export default AboutPage;