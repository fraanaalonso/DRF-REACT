
import axios from 'axios';
import Swal from 'sweetalert2';
import { blogAPI } from '../api/blogAPI'
import { login, checkingFinish, logout } from './types_actions';

export const startLogin = (email, password) => {
    return async(dispatch) => {
        axios.all([
            await blogAPI.post('auth/accounts/login/', {email, password}),
            await blogAPI.post('token/', {email, password}),
        ])
        .then((respAA) => {
            localStorage.setItem('access', respAA[1].data.access);
            localStorage.setItem('refresh', respAA[1].data.refresh);
            localStorage.setItem('token-init-date', new Date().getTime());
            dispatch(login({
                uid: respAA[0].data.uid,
                email: respAA[0].data.user.email,
            }));
            
        })

    }
}


export const startRegister = (email, password, first_name, user_name) => {
    return async(dispatch) => {
        const resp = await blogAPI.post('auth/accounts/register/', {email, first_name, password, user_name});
        const {data} = resp;

        if( data.ok ){
            const Toast = Swal.mixin({
                toast: true,
                position: 'top',
                showConfirmButton: false,
                timer: 5000,
                heightAuto: '60px',
                timerProgressBar: true,
                didOpen: (toast) => {
                  toast.addEventListener('mouseenter', Swal.stopTimer)
                  toast.addEventListener('mouseleave', Swal.resumeTimer)
                }
              })
              
              Toast.fire({
                icon: 'success',
                title: 'Signed in successfully'
              })
              return;
        }
        else{
            Swal.fire('Error', 'User with this login or email already exists', 'error');
        }
    }
}


export const startChecking = () => {
    return async(dispatch, getState) => {
        const token = localStorage.getItem('refresh');
        const {uid, email} = getState().auth;
        const resp = await blogAPI.post('token/refresh/', {refresh: token});

        
        if( resp.status !== 200){
            return dispatch(logout())
        }

        if(token){
            localStorage.setItem('access', resp.data.access);
            localStorage.setItem('refresh', resp.data.refresh);
            localStorage.setItem('token-init-date', new Date().getTime() );

            dispatch(login({
                uid: uid,
                email: email
            }))
        }
        else{
            dispatch(checkingFinish());
        }

        

    }
}

export const startLogout = () =>{
    return async(dispatch) => {
        localStorage.clear();
        dispatch(logout());
    }
}