import React from 'react';

import Logo from './components/Logo';

import './Header.css';

const Header = () => {

    return (
        <div className='header'>
            <Logo></Logo>
            <div className='navMenu'> 
                <div className='navMenu__item'>
                    About Us
                </div>
            </div>
        </div>
    )
}

export default Header;