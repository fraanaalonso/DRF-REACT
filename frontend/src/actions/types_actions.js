import { types } from "../types/types"

export const login = ( user ) => ({
    type: types.login,
    payload: user
})