import React from 'react';

import Hero from './components/Hero';
import CardSection from './components/CardSection';

import './Page.css';


const Page = () => {
    return (<div className='page__wrapper'>
        <Hero></Hero>
        <CardSection></CardSection>
    </div>)
}


export default Page;