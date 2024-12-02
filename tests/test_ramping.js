import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        { duration: '10s', target: 5 }, // Підвищення до 5 користувачів
        { duration: '20s', target: 10 }, // Підвищення до 10 користувачів
        { duration: '10s', target: 0 }, // Зменшення до 0 користувачів
    ],
};

export default function () {
    http.get('http://127.0.0.1:8000/');
    sleep(1);
}