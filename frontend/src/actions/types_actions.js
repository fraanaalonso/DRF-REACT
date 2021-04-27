import { types } from "../types/types"

export const login = ( user ) => ({
    type: types.login,
    payload: user
})

export const checkingFinish = () => ({
    type: types.authCheckingFinish
})

export const logout = () => ({
    type: types.logout
})

