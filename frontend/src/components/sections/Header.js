import React from 'react'

export const Header = () => {

    const handleMenu = () => {
        const hamburguerContainer = document.querySelector('#header__main-nav');
        const links = document.querySelectorAll('.header__main-nav--links li')

        hamburguerContainer.classList.toggle('clicked'); /*we add this class to the container to manage the vertical menu*/
    
        links.forEach((link) => {
            link.classList.toggle('fade');
        })
    }
    return (
        <header id="header">
            <nav id="header__main-nav">
                <div className="header__main-nav--hamburger" onClick={ handleMenu }>
                    <div className="line line-1"></div>
                    <div className="line line-2"></div>
                    <div className="line line-3"></div>
                </div>

                <ul className="header__main-nav--links">

                    <li><a>Home</a></li>
                    <li><a>About</a></li>
                    <li><a>Projects</a></li>
                    <li><a>Services</a></li>
                    <li><a>Hire Me</a></li>
                    <li><a>Contact</a></li>

                </ul>
            </nav>
        </header>
    )
}
