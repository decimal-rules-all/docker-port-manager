import axios from 'axios';
import { Container } from 'types';

const API_URL = 'http://localhost:8000';

export const getContainers = async (): Promise<Container[]> => {
    const { data } = await axios.get<Container[]>(`${API_URL}/containers`);
    return data;
}