import Swal from "sweetalert2";
import { blogAPI } from "../api/blogAPI"
import { getProjects } from "./types_actions";


export const projectLoad = () => {
    return async(dispatch) => {
        const resp = await blogAPI.get('portfolio/projects/list_projects/');
        const projects = resp.data.posts;

        if(resp.data.ok){
            dispatch(getProjects(projects));
        }
        else{
            Swal.fire('Error', resp.data.statusText, 'error');
        }
    }
}