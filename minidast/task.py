
import requests

from celery import Celery
from config import BROKER_CONN_STR, API_URL, application_scanner as scanner

app = Celery("scan_task", broker=BROKER_CONN_STR)

def update_status(id: int, error: bool):
    try:
        headers = {'Content-Type': 'application/json'}
        res = requests.post(f"{API_URL}/scan/{id}/update-status", json={ "error_ocurred": error}, headers=headers)
        return res
    except:
        print(res.text)

def set_scan_result(id: int, result: str):
    try:
        headers = { 'Content-Type': 'application/json' }
        res = requests.post(f"{API_URL}/scan/{id}/result", json={ "result": result }, headers=headers)
        print("Scan")
        return res
    except:
        print(res.text)


@app.task
def scan_task(scan_id: int, urls: list):
    try:

        print(f"[TASK] - Updating status for id {scan_id}")
        res = update_status(scan_id, error=False)

        if res.status_code != 200:
            raise BaseException()

        for target in urls:
            print(f"Starting active scan to scan_id [{scan_id}] -target {target['url']}")
            scanner.start_scan(url=target['url'])

        
        result = scanner.get_results()
        set_scan_result(scan_id, result)            
        res = update_status(scan_id, error=False)


    except BaseException as e:
        ### setting scan status to error and futher actions can be assigned later
        res = update_status(scan_id, error=True)
        print(e)

        

    