import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api/';

export const blogAPI = axios.create({
    baseURL: baseURL
})

blogAPI.interceptors.request.use(
    async (config) => {
      const token = localStorage.getItem('access')
      if (token) {
        config.headers['Authorization'] = 'Bearer ' + token
      }

      return config
    },
    (error) => {
      return Promise.reject(error)
    }
  )