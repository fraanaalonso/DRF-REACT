import { types } from "../types/types"

export const login = ( user ) => ({
    type: types.login,
    payload: user
})

export const notAuthenticated = () => ({
    type: types.notAuthenticated
})