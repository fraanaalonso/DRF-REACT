import Swal from "sweetalert2";
import { blogAPI } from "../api/blogAPI"
import { getSkills } from "./types_actions";



export const skillLoad = () => {
    return async(dispatch)=> {
        const resp = await blogAPI.get('portfolio/skills/list_skills/');
        const skills = resp.data.posts;

        if( resp.data.ok ){
            dispatch(getSkills(skills));
        }
        else{
            Swal.fire('Error', resp.statusText, 'error');
        }
    }
}