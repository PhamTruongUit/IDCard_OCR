import React from 'react';
import PropTypes from 'prop-types';
import './Information.css'
import PhoneIphoneIcon from '@mui/icons-material/PhoneIphone';
import EmailIcon from '@mui/icons-material/Email';
import GitHubIcon from '@mui/icons-material/GitHub';
import FacebookIcon from '@mui/icons-material/Facebook';
Information.propTypes = {
    
};

const about = {
    id:[
        {
            name: 'Name',
            cs: 'Class',
            info: 'Information',
            image: 'IMG.URL', 
            fb: 'LinkFB',
            github: 'LinkGH',
            email: 'Link email',
        },
        {
            name: 'Name',
            cs: 'Class',
            info: 'Information',
            image: 'IMG.URL', 
            fb: 'LinkFB',
            github: 'LinkGH',
            email: 'Link email',
        },
        {
            name: 'Name',
            cs: 'Class',
            info: 'Information',
            image: 'IMG.URL', 
            fb: 'LinkFB',
            github: 'LinkGH',
            email: 'Link email',
        }
    ]
}

function Information(props) {
    return (
        <div className="container">
            <div className="row container1">
                <div className="character col-sm-12 col-md-12 col-lg-6 col-xl-6" >
                    <div className="icon-right"></div>
                    <div className="material-1">
                    <div className="avatar"></div>
                    </div>
                    <div className="material-2"></div>
                    <div className="material-3"></div>
                    <div className="material-4"></div>
                    <h2 className="name-avatar"> Sơn Trần</h2>
                    <ul className="skill">
                        <li>
                            ReactJS
                        </li>
                        <li>
                            WebDev
                        </li>
                        <li className="no-type">
                            <PhoneIphoneIcon style={{color: '#229f73', fontSize: 20}}/>
                            <span>0365-560-383</span>
                        </li>
                        <li className="no-type">
                            <EmailIcon style={{color: '#229f73', fontSize: 20}}/>
                            <span>18521351@gm.uit.edu.vn</span>
                        </li>
                        <li className="no-type">
                            <GitHubIcon style={{color: '#229f73', fontSize: 20}}/>
                            <span>github.com/Master2k0</span>
                        </li>
                        <li className="no-type">
                            <FacebookIcon style={{color: '#229f73', fontSize: 20}}/>
                            <span>facebook.com/HoangSon2402</span>
                        </li>
                    </ul>
                </div>
                <div className="character col-sm-12 col-md-12 col-lg-6 col-xl-6" >
                    <div className="material-1">
                    <div className="avatar"></div>
                    </div>
                    <div className="material-2"></div>
                    <div className="material-3"></div>
                    <div className="material-4"></div>
                    
                </div>
            </div>
        </div>
    );
}

export default Information;