import './header.css';
import React, { useRef, useEffect, useState }  from 'react';
import FilterIcon from '@mui/icons-material/Filter';
import PermIdentityIcon from '@mui/icons-material/PermIdentity';
import {Link} from 'react-router-dom';



export default function HeaderNavBar(props) {
    const [dimensions1, setdimensions1] = useState({width: 0, height: 0});
    const [dimensions2, setdimensions2] = useState({width: 0, height: 0});

    useEffect(()=>{
        const getWidthHeight = document.getElementsByClassName("hold");
        setdimensions1({width: getWidthHeight[0].offsetWidth, height: getWidthHeight[0].offsetHeight});
        setdimensions2({width: getWidthHeight[1].offsetWidth, height: getWidthHeight[1].offsetHeight});

    },[])
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
                            <Link to="/App" className="hold svg1  btn1">
                                <p>APP</p>
                                <svg className="svg_css" width={`${dimensions1.width}`} height={`${dimensions1.height}`} viewBox={`0 0 ${dimensions1.width} ${dimensions1.height}`}> 

                                <polyline points={`${Math.floor(dimensions1.width / 2)},0
                                    ${dimensions1.width},0
                                    ${dimensions1.width},${dimensions1.height}
                                    ${Math.floor(dimensions1.width/ 2)},${dimensions1.height}                            
                                `} />

                                <polyline points={`${dimensions1.width / 2},${dimensions1.height}  
                                    0,${dimensions1.height} 
                                    0,0
                                    ${dimensions1.width / 2},0
                                
                                `} />
                                </svg>
                            </Link>
                           
                        </li>

                        <li>
                            {/* <PermIdentityIcon /> */}
                            <Link to="Information" className="hold svg2  btn1">
                                <p>Information</p>
                                <svg className="svg_css" width={`${dimensions2.width}`} height={`${dimensions2.height}`} viewBox={`0 0 ${dimensions2.width} ${dimensions1.height}`}> 
                                <polyline points={`${Math.floor(dimensions2.width / 2)},0
                                    ${dimensions2.width },0
                                    ${dimensions2.width },${dimensions2.height}
                                    ${Math.floor(dimensions2.width/ 2)},${dimensions2.height}                            
                                `} />

                                <polyline points={`${dimensions2.width / 2},${dimensions2.height}  
                                    0,${dimensions2.height} 
                                    0,0
                                    ${dimensions2.width / 2},0

                                `} />
                                </svg>
                            </Link>
                        </li>
                    </ul>
                </div>
            </div>  
        </div>
    );
}

