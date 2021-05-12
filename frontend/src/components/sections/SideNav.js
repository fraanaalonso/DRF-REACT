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
                        <a href='https://www.facebook.com/Fran-Alonso-110594836979402'><i className="fab fa-facebook-f"></i></a>
                        <a href='https://twitter.com/alonso_f09'><i className="fab fa-twitter"></i></a>
                        <a href='https://www.linkedin.com/feed/'><i className="fab fa-linkedin-in"></i></a>
                        <a href='https://www.instagram.com/fraanaalonso/'><i className="fab fa-instagram"></i></a>
                        <a href='https://www.youtube.com/channel/UC_eAmK6Y_hrxijp0jhGc6Jg'><i className="fab fa-youtube"></i></a>
                        <a href='https://www.github.com/fraanaalonso'><i className="fab fa-github"></i></a>
                    </ul>
                </div>
        </aside>
    )
}
