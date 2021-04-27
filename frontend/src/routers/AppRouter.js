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


  
  if(checking){
    return <h5>Wait...</h5>
  }

  return (
    <Router>
        <div>
        <Switch>
                <PublicRoute path="/auth" component={AuthRouter} isLoggedIn={!!uid}/>
                <PrivateRoute exact path='/' component={DashboardScreen} isLoggedIn={!!uid} />
                <Redirect to="/" />
        </Switch>
        </div>
    </Router>
  );
}