import './header.css';
import React from 'react';
import FilterIcon from '@mui/icons-material/Filter';
import PermIdentityIcon from '@mui/icons-material/PermIdentity';
export default function HeaderNavBar(props) {
    return (
        <div className="background-navbar">
            <div className="header-navbar container">
                <h1>
                    PassPort OCR
                </h1>
                <div className="header-navbar__list">
                    <ul>
                        <li>
                            <FilterIcon/>
                            App
                        </li>
                        <li>
                            <PermIdentityIcon />
                            Infomation
                        </li>
                    </ul>
                </div>
            </div>  
        </div>
    );
}

