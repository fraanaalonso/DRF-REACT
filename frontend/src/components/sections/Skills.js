import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { skillLoad } from '../../actions/skill';

export const Skills = () => {

    const dispatch = useDispatch();
    
    useEffect(() => {
        dispatch(skillLoad());
    }, [dispatch]);

    const {skills} = useSelector(state => state.skill);
    return (
        <section id="skills">
        
            <div className="skills__coding">
                <h3 className="skills__coding--title">Skills</h3>

                {
                    skills.map( (skill, i) => (
                        <div key={skill.uid}>
                            <h4>{ skill.name }</h4>
                            <div className="skills__coding--progress">
                                <span className={`skills__coding--progess__${i + 1}`} style={{ width: '80%'}}>
                                
                                </span>
                            </div>
                        </div>
                        
                    ))
                }
                
                
            </div>
        </section>
    )
}


