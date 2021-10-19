import EmailIcon from '@mui/icons-material/Email';
import FacebookIcon from '@mui/icons-material/Facebook';
import GitHubIcon from '@mui/icons-material/GitHub';
import PhoneIphoneIcon from '@mui/icons-material/PhoneIphone';
import React from 'react';
import sonJPG from '../../img/avatar/son.jpg';
import truongJPG from '../../img/avatar/truong.jpg';
import TthinhJPG from '../../img/avatar/tthinh.jpg';
import VthinhJPG from '../../img/avatar/vthinh.jpg';
import './Information.css';

import AOS from 'aos';
import 'aos/dist/aos.css';

AOS.init(
);
Information.propTypes = {
    
};

const about = [
        {
            name: 'Trường Phạm',
            skill: ['Computer Sciene','Web Dev'],
            image: truongJPG, 
            fb: 'facebook.com/phamtruonguit',
            github: 'github.com/PhamTruongUit',
            email: '18521571@gm.uit.edu.vn',
            phone: '0355-226-567',
            color: 'linear-gradient(to left top, #d9e021, #a3d43f, #74c457, #49b368, #229f73)',
            color1: '#229f73',
            cn: 'top-left',
            fade: 'new-animation-1',
        },
        {
            name: 'Nguyễn T.Thịnh',
            skill: ['Fontend Dev',''],
            image: TthinhJPG, 
            fb: 'facebook.com/thinhntr',
            github: 'github.com/thinhntr',
            email: '18521447@gm.uit.edu.vn',
            phone: '0378-902-690',
            color: 'linear-gradient(to left top, #4ca4f0, #8393ee, #b47ddb, #d864b8, #ec4e8a)',
            color1: '#ec4e8a',
            cn: 'top-right',
            fade: 'new-animation-2',
        },
        {
            name: 'Sơn Trần',
            skill: ['Fontend Dev',''],
            image: sonJPG, 
            fb: 'facebook.com/HoangSon2402',
            github: 'github.com/Master2k0',
            email: '18521351@gm.uit.edu.vn',
            phone: '0365-560-383',
            color: 'linear-gradient(to left top, #f0a44c, #ff877d, #f77fb9, #b78fe5, #4e9eec)',
            color1: '#4e9eec',
            cn: 'bottom-left',
            fade: 'new-animation-3',
        },
        {
            name: 'Nguyễn V.Thịnh',
            skill: ['Fontend Dev','BayLAg'],
            image: VthinhJPG, 
            fb: 'facebook.com/HoangSon2402',
            github: 'github.com/NguyenVanThinh2000',
            email: '18521448@gm.uit.edu.vn',
            phone: '0971-449-695',
            color: 'linear-gradient(to left top, #6fc404, #d89c00, #ff6448, #ff49a4, #ac70ef)',
            color1: '#ac70ef',
            cn: 'bottom-right',
            fade: 'new-animation-4',
        }
    ]

function Information(props) {
    return (
        <div className="container">
            <div className="row container1">
                {/* <div className="character top-left col-sm-12 col-md-12 col-lg-6 col-xl-6" >
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
                </div> */}

                {about.map( char =>{
                    return(
                        <div data-aos={`${char.fade}`} data-aos-duration="2000" className={`character ${char.cn} col-sm-12 col-md-12 col-lg-6 col-xl-6 col-xxl-6`}>
                            <div className="icon-right"></div>
                            <div className="material-1" style={{backgroundImage: `${char.color}`,}}>
                                <div className="avatar" style={{backgroundImage: `url(${char.image})`}}></div>
                            </div>
                            <div className="material-2" style={{backgroundImage: `${char.color}`,}}></div>
                            <div className="material-3" style={{backgroundImage: `${char.color}`,}}></div>
                            <div className="material-4" style={{backgroundImage: `${char.color}`,}}></div>
                            <h2 className="name-avatar">{char.name}</h2>
                            <ul className="skill">
                                {char.skill.map(sk =>{
                                    if(sk !== ''){
                                        return(
                                            <li>{sk}</li>
                                        )
                                    }
                                })}
                                <li className="no-type">
                                    <PhoneIphoneIcon style={{color: `${char.color1}`, fontSize: 20}}/>
                                    <span>{char.phone}</span>
                                </li>
                                <li className="no-type">
                                    <EmailIcon style={{color: `${char.color1}`, fontSize: 20}}/>
                                    <span>{char.email}</span>
                                </li>
                                <li className="no-type">
                                    <GitHubIcon style={{color: `${char.color1}`, fontSize: 20}}/>
                                    <span>{char.github}</span>
                                </li>
                                <li className="no-type">
                                    <FacebookIcon style={{color: `${char.color1}`, fontSize: 20}}/>
                                    <span>{char.fb}</span>
                                </li>
                            </ul>
                        </div>
                    )
                })}                
            </div>
        </div>
    );
}

export default Information;