import React from "react";

import "./Card.css";


const Card = (props) => {
  return (
    <div className="card__wrapper">
        <div className='card__header'>
          Bitcoin
        </div>
        <img className='card__image' src="https://png.pngtree.com/png-vector/20220527/ourmid/pngtree-bitcoin-logo-design-template-png-image_4749408.png"></img>
        <div className="card__content">
          <div>Place: #1</div>
          <div>Place: #1</div>
          <div>Place: #1</div>
          <div>Place: #1</div>
        </div>
    </div>
  );
};

export default Card;
