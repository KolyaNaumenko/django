import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    vus: 10, // Кількість одночасних користувачів
    duration: '30s', // Тривалість тесту
};

export default function () {
    http.get('http://127.0.0.1:8000/'); // URL вашого проєкту
    sleep(1); // Затримка між запитами
}