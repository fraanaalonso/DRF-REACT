import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Redirect
} from "react-router-dom";
import { AuthRouter } from "./AuthRouter";
import { PublicRoute } from "./PublicRoute";

export const AppRouter = () => {
  return (
    <Router>
        <div>
        <Switch>
                <PublicRoute path="/auth" component={AuthRouter} />
                <Redirect to="/auth/login" />
        </Switch>
        </div>
    </Router>
  );
}