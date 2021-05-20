
import React from 'react'
import { types } from '../types/types';



const initialState = {
    projects: []
}



export const projectReducer = ( state = initialState, action) => {
    
    switch (action.type) {
        case types.projectLoaded:
            return {
                ...state,
                projects: action.payload
            }
            break;
    
        default:
            return state;
    }
    
}


