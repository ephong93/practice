import React from 'react';
import { useState } from 'react';

const Counter = () => {
    const [ count, setCount ] = useState(0);

    const onClickPlus = () => {
        setCount(count+1);
    }

    const onClickMinus = () => {
        setCount(count-1);
    }

    return (
        <div className="counter">
            <h1>I'm counter</h1>
            <button 
                className="plus-button"
                onClick={ onClickPlus }>+</button>
            <p className="count">{ count }</p>
            <button 
                className="minus-button"
                onClick={ onClickMinus }>-</button>
        </div>
    );
}

export default Counter;