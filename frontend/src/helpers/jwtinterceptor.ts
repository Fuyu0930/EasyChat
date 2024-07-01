import axios, { AxiosInstance } from 'axios';
import { useNavigate } from 'react-router-dom';
import { BASE_URL } from '../config';

const API_BASE_URL = BASE_URL;

const useAxiosWithInterceptor = (): AxiosInstance => {
    const jwtAxios = axios.create({ baseURL: API_BASE_URL });
    const navigate = useNavigate();

    // Allows us to intercept and modify the http requests and responses
    // Return the response to the application
    jwtAxios.interceptors.response.use(
        (response) => {
            return response; // it will be sent to the application
        },
        async (error) => {
            const originalRequest = error.config;
            // 401 Unauthorized
            if (error.response?.status === 403) {
                // redirect the user
                const goRoot = () => navigate("/test");
                goRoot(); // Navigate to the home page
            }
            throw error;
        }
    );

    return jwtAxios;
}

export default useAxiosWithInterceptor;
