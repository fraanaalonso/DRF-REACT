import { types } from "../types/types";

const intialState = {
    checking: true,
    uid: null,
    email: null

}


export const authReducer = (state=intialState, action) => {
    switch (action.type) {
        case types.login:
            return {
                ...state,
                checking: false,
                ...action.payload
            }
        case types.logout:
            return {
                checking: false
            }
        default:
            break;
    }
}
