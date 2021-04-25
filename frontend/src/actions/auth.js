
import Swal from 'sweetalert2';
import { blogAPI } from '../api/blogAPI'
import { login } from './types_actions';

export const startLogin = (email, password) => {
    return async(dispatch) => {
        const { data } = await blogAPI.post('auth/accounts/login/', {email, password});

        if ( data.ok ){
            localStorage.setItem('token', data.token.access);
            localStorage.setItem('token-init-date', new Date().getTime());

            dispatch(login({
                uid: data.uid,
                email: data.user.email
            }))
        }else{
            Swal.fire('Error', `${ data.msg.email } \n ${data.msg.password}` , 'error');
        }

    }
}