import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  BrowserRouter as Router,
  Switch,
  Redirect
} from "react-router-dom";
import { startChecking } from "../actions/auth";
import { DashBoardScreen } from "../components/DashBoardScreen";
import { AuthRouter } from "./AuthRouter";
import { PrivateRoute } from "./PrivateRoute";
import { PublicRoute } from "./PublicRoute";

export const AppRouter = () => {

  const dispatch = useDispatch();
  const { status, uid, email } = useSelector(state => state.auth)
  
  

  return (
    <Router>
        <div>
        <Switch>
                <PublicRoute path="/auth" component={AuthRouter} isLoggedIn={!!uid}/>
                <PrivateRoute exact path='/' component={DashBoardScreen} isLoggedIn={!!uid} />
                <Redirect to="/auth/login" />
        </Switch>
        </div>
    </Router>
  );
}