import time
from scanner.Scanner import Scanner
from zapv2 import ZAPv2

class ZaproxyScanner(Scanner):
    
    def __init__(self, proxies = {}) -> None:
        
        self.zap = zap = ZAPv2(proxies=proxies)
        self.scanId = None
        self.results = []

        super().__init__()

    def start_scan(self, url):
        
        self.scan_id = self.zap.ascan.scan(url)
        while self.zap.ascan.status(self.scan_id) < "100":
            print('Scan progress %: {}'.format(self.zap.ascan.status(self.scan_id)))

        self.results.append({"alerts": str(self.zap.core.alerts())})

    # this could be in another family of class with other ways to get the result
    def get_results(self):

        alert_text = ""
        for result in self.results:
            alert_text += f"{result}\n"

        return alert_text 
