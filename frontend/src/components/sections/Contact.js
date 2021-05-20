import React from 'react'
import Swal from 'sweetalert2';
import { useForm } from '../../hooks/useForm';

import validator from 'validator';

export const Contact = () => {

    const {values, handleInputChange } = useForm({
        name: '',
        email: '',
        subject: '',
        content: '',
    })

    const { name, email, subject, content } = values;

    const handleSubmit = e => {
        e.preventDefault();

        if( validator.isEmpty(name) ||
            validator.isEmpty(email) ||
            validator.isEmpty(subject) ||
            validator.isEmpty(content) ){
                Swal.fire('Error', 'You must fill all the fields', 'error');
                return;
            }
        
        if( !validator.isEmail(email) ){
            Swal.fire('Error', 'Email not valid', 'error');
            return;
        }
        
    }
    return (
        <section id="contact">
            <form className="contact__form" onSubmit={ handleSubmit }>
                <input type="text" placeholder='Name' name='name' value= {name} onChange={ handleInputChange} />
                <input type="text" placeholder='Email' name='email' value={email}  onChange={ handleInputChange} />
                <input type="text" placeholder='Subject' name='subject' value={ subject } onChange={ handleInputChange } />
                <textarea placeholder='Write here...' name='content' value={ content } onChange={ handleInputChange }></textarea>

                <input type="submit" value='Submit' />
            </form>
        </section> 
    )
}
