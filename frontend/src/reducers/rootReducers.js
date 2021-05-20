import { combineReducers } from "redux";
import { authReducer } from "./authReducer";
import { projectReducer } from "./projectReducer";
import { skillReducer } from "./skillReducer";

export const rootReducers = combineReducers({
    auth: authReducer,
    skill: skillReducer,
    project: projectReducer,
});
