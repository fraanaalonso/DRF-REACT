import React from 'react'
import about_me from '../../assets/about.jpg'
export const About = () => {
    return (
        <section id='about'> 
            <div className="about__pic">
                <img src={ about_me } width={ 400 } alt='About' />
            </div>

            <div className="about__content">
                <h2 className="about__content--title">About Me</h2>

                <div className='separator'></div>
                <p className="about__content--para">

                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.                        
                
                </p>
                <a className="about__content--link">Read More</a>
            </div>
        </section>
    )
}
