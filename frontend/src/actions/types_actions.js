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

export const getSkills = (skills) => ({
    type: types.skillLoaded,
    payload: skills
}) 

export const getProjects = (projects) => ({
    type: types.projectLoaded,
    payload: projects
})

