import React from 'react';
import Image from '../assets/ppal_img.png'; 

function Logo() {
    return (
        <div className="logo-container">
            <img src={Image} alt="Protein Pal Logo" className="logo-image" />
            <h1 className="logo-text">Protein Pal</h1> 
        </div>
    );
}

export default Logo;
