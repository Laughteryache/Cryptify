import React from 'react';

import Logo from './components/Logo';
import navMenu from './components/navMenu';

import './Header.css';

const Header = () => {

    return (
        <div className='header'>
            <Logo></Logo>
            test
            <navMenu></navMenu>
        </div>
    )
}

export default Header;