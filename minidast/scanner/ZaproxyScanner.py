import time

from scanner.Scanner import Scanner
from scanner.Result import Result
from zapv2 import ZAPv2

class ZaproxyScanner(Scanner):
    
    def __init__(self, proxies = {}) -> None:
        
        self.zap = ZAPv2(proxies=proxies)
        self.scan_id = None
        self.results = []

        super().__init__()

    def start_scan(self, url):

        scanID = self.zap.spider.scan(url)
        while int(self.zap.spider.status(scanID)) < 100:
            print('Spider progress %: {}'.format(self.zap.spider.status(scanID)))
            time.sleep(2)

        
        self.scan_id = self.zap.ascan.scan(url)
        while self.zap.ascan.status( int(self.scan_id)) < "100":
            print('Scan progress %: {}'.format(self.zap.ascan.status(self.scan_id)))
            time.sleep(2)

        self.results = self.zap.core.alerts(baseurl=url)


    # this could be in another family of class with other ways to get the result
    def get_results(self):

        result_list = []
        for data in self.results:
            result = Result(
                url         = data.get("url", None),
                description = data.get("description", None),
                risk        = data.get("risk", None)
            )
            result_list.append(result.to_dict())
        return result_list
