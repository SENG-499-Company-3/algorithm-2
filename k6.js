import http from 'k6/http';
import { sleep } from 'k6';

const PROD = false;

const prod_url = 'http://52.39.88.189:8080/schedule';
const local_url = 'http://localhost:8080/schedule';

export default function () {
    let url = local_url;
    if(PROD){
        url = prod_url;  
    }
    const data = [
            {
                "course": "csc115",
                "Term" : [5, 9, 1],
                "Year" : 2024,
                "pastEnrollment": [
                    {
                        "year": 2017,
                        "term": 5,
                        "size": 75
                    }
                ]
            }
        ];
    
    let res = http.post(url, JSON.stringify(data), {
        headers: { 'Content-Type': 'application/json' },
    });

    sleep(1);
}
