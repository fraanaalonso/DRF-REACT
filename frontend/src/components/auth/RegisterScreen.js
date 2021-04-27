import React from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import { Copyrigth } from './Copyrigth';
import { useStylesRegister } from '../../styles/components/stylesLogin';
import { useForm } from '../../hooks/useForm';
import { useDispatch } from 'react-redux';
import { startRegister } from '../../actions/auth';
import Swal from 'sweetalert2';
import validator from 'validator'

export const RegisterScreen = () => {
  const classes = useStylesRegister();
  const dispatch = useDispatch()

  const { values, handleInputChange} = useForm({
    username:'',
    firstname: '',
    email:'',
    password: '',
    password_conf: '',
  });

  const { firstname, username, email, password, password_conf } = values;

  const handleSubmit = (e) => {
    e.preventDefault();

    if(!validator.isEmail( email ) ){
      Swal.fire('Error', 'Email format is not correct', 'error');
      return;
    }

    if(validator.isEmpty( email ) || validator.isEmpty( username ) || validator.isEmpty( firstname ) || validator.isEmpty( password ) || validator.isEmpty( password_conf )){
      Swal.fire('Error', 'There are empy fields','error');
      return;
    }

    if( password !== password_conf){
      Swal.fire('Error', 'Passwords do not match', 'error');
      return;
    }
    dispatch(startRegister(email, password, firstname, username));
  }

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>
        <form onSubmit={ handleSubmit } className={classes.form} noValidate>
          <Grid container spacing={2}>
          <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="firstname"
                label="First Name"
                name="firstname"
                autoComplete="lname"
                value={firstname}
                onChange={ handleInputChange }
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="username"
                label="User Name"
                name="username"
                autoComplete="lname"
                value={username}
                onChange={ handleInputChange }
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                value={email}
                onChange={ handleInputChange }
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="password"
                type='password'
                label="Password"
                name="password"
                value={password}
                onChange={ handleInputChange }
              />
            </Grid>

            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="password_conf"
                label="Password Confirmation"
                type="password"
                id="password2"
                autoComplete="current-password"
                value={password_conf}
                onChange={ handleInputChange }
              />
            </Grid>
            <Grid item xs={12}>
              <FormControlLabel
                control={<Checkbox value="allowExtraEmails" color="primary" />}
                label="I want to receive inspiration, marketing promotions and updates via email."
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Sign Up
          </Button>
          <Grid container justify="flex-end">
            <Grid item>
              <Link href="/auth/login" variant="body2">
                Already have an account? Sign in
              </Link>
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={5}>
        <Copyrigth />
      </Box>
    </Container>
  );
}