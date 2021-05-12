import React from 'react'
import logo from '../../assets/logo_1.jpg'
export const SideNav = () => {
    return (
        <aside id="side-nav">
                <div className="side-nav__content">
                    <div className="side-nav__content--logo">
                        <img src={logo} alt="logo" width={200}/>
                    </div>

                    <ul className="side-nav__content--social">
                        <a><i className="fab fa-facebook-f"></i></a>
                        <a><i className="fab fa-twitter"></i></a>
                        <a><i className="fab fa-linkedin-in"></i></a>
                        <a><i className="fab fa-instagram"></i></a>
                        <a><i className="fab fa-youtube"></i></a>
                    </ul>
                </div>
        </aside>
    )
}
