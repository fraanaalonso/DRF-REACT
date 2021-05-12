import React, { useState } from 'react'
import about_me from '../../assets/about.jpg'
export const About = () => {
    const [button, setButton] = useState('Read More');
    const [show, setShow] = useState(false)

    const handleInOut = () => {
        if( !show ){
            setShow(true);
            setButton('Hide');
            return;
        }

        setShow(false);
        setButton('Read More')
        
    }
    return (
        <section id='about'> 
            <div className="about__pic">
                <img src={ about_me } width={ 400 } alt='About' />
            </div>

            <div className="about__content">
                <h2 className="about__content--title">About Me</h2>

                <div className='separator'></div>

                <div className="about__content--div">
                    <p className="about__content--para">                       
                        My name is Fran Alonso and I was born in Manneddorf, Switzerland in 1997.
                        In 2015, I start with a double degree in computer engineering and businesss 
                        management. Throughout the process, I learnt a bunch of new technologies and programmming languages
                        that help me to develop applications in different environments(Web, Desktop, CLI). Also, I took different online formations about software design to have a metodology when it comes to develop new functionalities.
                    </p>

                    <p className='about__content--para' id='hidden-para' style={{display: !show ? 'none' : ''}}>
                        Moreover, my passion and activity is software development but I always find some time to do other things like 
                        Youtube content about financial education. You can check out my channel by clicking on the youtube icon placed on the side bar. 
                    </p>
                </div>
                
                <a onClick={ handleInOut } className="about__content--link">{ button }</a>
            </div>
        </section>
    )
}
