import React from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import { AccountCircle } from '@material-ui/icons'
import Typography from '@material-ui/core/Typography';
import { useStylesLogin } from '../../styles/components/stylesLogin';
import { Copyrigth } from './Copyrigth';
import { useForm } from '../../hooks/useForm';
import { useDispatch } from 'react-redux';
import { startLogin } from '../../actions/auth';



export const LoginScreen = () => {
  const dispatch = useDispatch()
  const classes = useStylesLogin();
  const { values, handleInputChange} = useForm({
    email:'fraloal97@email.com',
    password: 'testpass123',
  });

  const { email, password } = values;

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(startLogin(email, password));
  }

  return (
    <Grid container component="main" className={classes.root}>
      <CssBaseline />
      <Grid item xs={false} sm={4} md={7} className={classes.image} />
      <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <AccountCircle />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <form onSubmit={ handleSubmit } className={classes.form} noValidate >
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name='email'
              autoComplete="email"
              autoFocus
              value={ email }
              onChange={ handleInputChange }
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name='password'
              label="Password"
              type="password"
              id="password"
              value={ password }
              autoComplete="current-password"
              onChange={ handleInputChange }
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link href="/auth/register" variant="body2">
                  Create a new account
                </Link>
              </Grid>
            </Grid>
            <Box mt={5}>
              <Copyrigth />
            </Box>
          </form>
        </div>
      </Grid>
    </Grid>
  );
}