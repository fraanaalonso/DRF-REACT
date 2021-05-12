import React from 'react'
import { About } from './sections/About'
import { Contact } from './sections/Contact'
import { Header } from './sections/Header'
import { Services } from './sections/Services'
import { ShowCase } from './sections/ShowCase'
import { SideNav } from './sections/SideNav'
import { Skills } from './sections/Skills'
import { Work } from './sections/Work'

export const IndexScreen = () => {
    return (
        <div className='body'>
            <SideNav />

            <main style={{flex: 1}}>
                <Header />

                <ShowCase />

                <Work /> 

                <About />


                <Services />


                <Skills />


                <Contact />  
            </main>
        </div>
    )
}
