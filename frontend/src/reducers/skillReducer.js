import { types } from "../types/types";

/*

    skill = {
        name: '',
        progresion: ''
    }

*/
const initialState = {
    skills: []
}


export const skillReducer = (state = initialState, action) =>{
    switch (action.type) {
        case types.skillLoaded:
            return {
                ...state,
                skills: action.payload
            }
    
        default:
            return state
    }
}