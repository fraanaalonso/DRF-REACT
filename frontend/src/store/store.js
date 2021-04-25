import {createStore, combineReducers, applyMiddleware, compose } from 'redux';
import { authReducer } from '../reducers/authReducer';
import thunk from 'redux-thunk';

//composeEnhancers copied from https://github.com/zalmoxisus/redux-devtools-extension#usage
const composeEnhancers = (typeof window !== 'undefined' && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__) || compose;
const reducers = combineReducers({
    auth: authReducer,
})

export const store = createStore(
    reducers,
    composeEnhancers(applyMiddleware( thunk ))
);