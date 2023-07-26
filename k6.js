import http from 'k6/http';
import { sleep } from 'k6';
import { tagWithCurrentStageIndex } from 'https://jslib.k6.io/k6-utils/1.3.0/index.js';
import { htmlReport } from    "https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js";

const PROD = false;

const prod_url = 'http://52.39.88.189:8080/schedule';
const local_url = 'http://localhost:8080/schedule';

export const options = {

  stages: [

    { duration: '30s', target: 1 },
    { duration: '30s', target: 5 },
    { duration: '30s', target: 10 },
    { duration: '30s', target: 15 },
    { duration: '30s', target: 20 },
    { duration: '30s', target: 25 },
    { duration: '30s', target: 30 },
    { duration: '30s', target: 35 },
    { duration: '30s', target: 40 },
    { duration: '30s', target: 45 },
    { duration: '30s', target: 50 },
    { duration: '30s', target: 55 },
    { duration: '30s', target: 60 },
    { duration: '30s', target: 65 },
    { duration: '30s', target: 70 },
    { duration: '30s', target: 75 },
    { duration: '30s', target: 80 },
    { duration: '30s', target: 85 },
    { duration: '30s', target: 90 },
    { duration: '30s', target: 95 },
    { duration: '30s', target: 100 },

  ],

};


export function handleSummary(data) {
    return {
        'TestSummaryReport.html': htmlReport(data, { debug: true })
    };
}


export default function () {
    tagWithCurrentStageIndex()

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
