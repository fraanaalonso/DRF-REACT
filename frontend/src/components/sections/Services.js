import React from 'react'

export const Services = () => {
    return (
        <section id="services">
            <div className="service service__service-1">
                <i className="fas fa-quidditch"></i>
                <h3 className="services--title services__service-1--title">
                    UI Design
                </h3>

                <p className="services--para services__service-1--para">
                    Flexbox, Grid and Sass
                </p>
            </div>
            <div className="service service__service-2">
                <i className="fas fa-tasks"></i>
                <h3 className="services--title services__service-2--title">
                    Web Development
                </h3>

                <p className="services--para services__service-2--para">
                    React and Django Rest Framework
                </p>
            </div>
            <div className="service service__service-3">
                <i className="fas fa-project-diagram"></i>
                <h3 className="services--title services__service-3--title">
                    Software Design
                </h3>

                <p className="services--para services__service-3--para">
                    Unified Process
                </p>
            </div>
            
        </section>
    )
}
