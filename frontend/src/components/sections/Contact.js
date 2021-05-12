import React from 'react'

export const Contact = () => {
    return (
        <section id="contact">
            <form className="contact__form">
                <input type="text" placeholder='Name' />
                <input type="email" placeholder='Email' />
                <input type="text" placeholder='Subject' />
                <textarea name="message" placeholder='Write here...'></textarea>

                <input type="submit" value='Submit' />
            </form>
        </section> 
    )
}
