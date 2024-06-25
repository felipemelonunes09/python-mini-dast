
import requests

from celery import Celery
from config import BROKER_CONN_STR, API_URL, application_scanner as scanner

app = Celery("scan_task", broker=BROKER_CONN_STR)

def update_status(id: int, error: bool):
    try:
        headers = {'Content-Type': 'application/json'}
        res = requests.post(f"{API_URL}/scan/{id}/update-status", json={ "error_ocurred": error}, headers=headers)
        print(res.text)
        return res
    except Exception as e:
        print(e)

def send_scan_results(id: int, result: list):
    try:
        headers = {'Content-Type': 'application/json'}
        res = requests.post(f"{API_URL}/scan/{id}/result", json={ "results": result }, headers=headers)
        print(res.text)
        return res
    except Exception as e :
        print(e)


@app.task
def scan_task(scan_id: int, urls: list):
    try:

        print(f"Updating status for id {scan_id}")
        res = update_status(scan_id, error=False)

        if res.status_code != 200:
            raise Exception()

        for target in urls:
            print(f"Updating Starting active scan to scan_id [{scan_id}] -target {target['url']}")
            scanner.start_scan(url=target['url'])

        
        result_list = scanner.get_results()
        res = send_scan_results(scan_id, result_list)           
        
        if res.status_code != 200:
            raise Exception()

        res = update_status(scan_id, error=False)

    except Exception as e:
        ### setting scan status to error and futher actions can be assigned later
        res = update_status(scan_id, error=True)
        print(e)

        

    