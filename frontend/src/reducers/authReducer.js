import { types } from "../types/types";

const status = {
    checking: 'checking',
    auth: 'authenticated',
    notAuth: 'not-authenticated',
}

const intialState = {
    status: status.checking,
    uid: null,
    email: null

}


export const authReducer = (state=intialState, action) => {
    switch (action.type) {
        case types.login:
            return {
                ...state,
                status: 'authenticated',
                ...action.payload
            }
        case types.logout:
            return {
                status: 'not-authenticated'
            }
        case types.notAuthenticated:
            return {
                ...state,
                status: 'not-authenticated'
            }
        default:
            return state;
    }
}
