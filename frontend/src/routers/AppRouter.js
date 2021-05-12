import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  BrowserRouter as Router,
  Switch,
  Redirect
} from "react-router-dom";
import { startChecking } from "../actions/auth";
import { DashboardScreen } from "../components/dashboard/DashBoardScreen";
import { AuthRouter } from "./AuthRouter";
import { PrivateRoute } from "./PrivateRoute";
import { PublicRoute } from "./PublicRoute";

export const AppRouter = () => {

  const dispatch = useDispatch();
  const { checking, uid } = useSelector(state => state.auth);

  useEffect(() => {
    dispatch(startChecking());
  }, [dispatch]);


  return (
    <Router>
        <div>
        <Switch>
                <PublicRoute path="/" component={AuthRouter} isLoggedIn={!!uid}/>
                <Redirect to="/index" />
        </Switch>
        </div>
    </Router>
  );
}