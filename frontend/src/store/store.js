import {createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import { authReducer } from '../reducers/authReducer';
import { rootReducers } from '../reducers/rootReducers';

//composeEnhancers copied from https://github.com/zalmoxisus/redux-devtools-extension#usage
const composeEnhancers = (typeof window !== 'undefined' && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__) || compose;

export const store = createStore(
    authReducer,
    composeEnhancers(applyMiddleware( thunk ))
);