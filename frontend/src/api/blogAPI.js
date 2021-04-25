import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api/';

export const blogAPI = axios.create({
    baseURL: baseURL
})