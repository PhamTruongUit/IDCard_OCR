import './header.css';
import React, { useRef, useEffect, useState }  from 'react';
import FilterIcon from '@mui/icons-material/Filter';
import PermIdentityIcon from '@mui/icons-material/PermIdentity';
import {Link, NavLink} from 'react-router-dom';



export default function HeaderNavBar(props) {
    // const [dimensions1, setdimensions1] = useState({width: 0, height: 0});
    // const [dimensions2, setdimensions2] = useState({width: 0, height: 0});

    // useEffect(()=>{
    //     const getWidthHeight = document.getElementsByClassName("hold");
    //     setdimensions1({width: getWidthHeight[0].offsetWidth, height: getWidthHeight[0].offsetHeight});
    //     setdimensions2({width: getWidthHeight[1].offsetWidth, height: getWidthHeight[1].offsetHeight});

    // },[])
    return (
        <div className="background-navbar">
            <div className="header-navbar container">
                <h1>
                    PassPort OCR
                </h1>
                <div className="header-navbar__list">
                    <ul>
                        <li>
                            {/* <FilterIcon/> */}
                            <NavLink to="/" exact={true} 
                                     className="hold svg1  btn1"
                                     style={isActive => ({
                                        color: isActive ? "#FFE9CF" : "white"
                                      })} 
                            >
                                <p>APP</p>
                                <svg className="svg_css" width={`53px`} height={`34px`} viewBox={`0 0 53 34`}> 

                                <polyline points={`${Math.floor(53 / 2)},0
                                    52,0
                                    53,34
                                    ${Math.floor(53/ 2)},34                            
                                `} />

                                <polyline points={`${53 / 2},${34}  
                                    0,${34} 
                                    0,0
                                    ${53 / 2},0
                                
                                `} />
                                </svg>
                            </NavLink>
                           
                        </li>

                        <li>
                            {/* <PermIdentityIcon /> */}
                            <NavLink to="/Information" 
                                     className="hold1 svg2  btn1" 
                                     style={isActive => ({
                                        color: isActive ? "#FFE9CF" : "white"
                                      })} 
                            >
                                <p>Information</p>
                                <svg className="svg_css" width={`154px`} height={`34px`} viewBox={`0 0 154 34`}> 
                                <polyline points={`${Math.floor(154 / 2)},0
                                    154,0
                                    154,34
                                    ${Math.floor(154/ 2)},34                            
                                `} />

                                <polyline points={`${154 / 2},34
                                    0,34
                                    0,0
                                    ${154 / 2},0

                                `} />
                                </svg>
                            </NavLink>
                        </li>
                    </ul>
                </div>
            </div>  
        </div>
    );
}

