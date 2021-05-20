import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { projectLoad } from '../../actions/project'
import logo from '../../assets/logo_1.jpg'


export const Work = () => {

    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(projectLoad());
    }, [dispatch]);

    const { projects } = useSelector(state => state.project)
    console.log( projects )
    return (
        <section id='work'>
            {
                projects.map((project, i) => (
                    <div className="work__card">
                        <img src={ logo } width={400} alt="Logo" />
                    </div>
                ))
            }
        </section>  
    )
}
