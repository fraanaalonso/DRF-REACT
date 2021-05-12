import React from 'react'
import { Switch, Route, Redirect} from 'react-router-dom'
import { LoginScreen } from '../components/auth/LoginScreen'
import { RegisterScreen } from '../components/auth/RegisterScreen'
import { IndexScreen } from '../components/IndexScreen'


export const AuthRouter = () => {
    return (
            <Switch>
                    <Route exact path="/auth/login" component={LoginScreen} />
                    <Route exact path="/auth/register" component={RegisterScreen} />
                    <Route exact path='/index' component={IndexScreen} />
                    <Redirect to="/index" />
            </Switch>
    )
}
