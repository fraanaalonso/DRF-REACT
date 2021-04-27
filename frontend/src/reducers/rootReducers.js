import { combineReducers } from "redux";
import { authReducer } from "./authReducer";

export const rootReducers = combineReducers({
    auth: authReducer,
});
