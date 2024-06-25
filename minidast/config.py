
import os

from scanner.ZaproxyScanner import ZaproxyScanner

##
## Broker configuration 
##

BROKER_HOST             = os.environ.get('BROKER_HOST')
BROKER_PORT             = os.environ.get('BROKER_PORT')
BROKER_IDENTIFICATION   = os.environ.get('BROKER_IDENTIFICATION')

BROKER_CONN_STR = f"{BROKER_IDENTIFICATION}://{BROKER_HOST}:{BROKER_PORT}/0"

###
### Api configuration
###

API_HOST    = os.environ.get('API_HOST') 
API_PORT    = os.environ.get('API_PORT')

API_URL     = f'http://{API_HOST}:{API_PORT}'

##
## Scanner configuration
##

SCANNER_PROXY_HTTP    = os.environ.get('SCANNER_PROXY_HTTP') 
SCANNER_PROXY_HTTPS   = os.environ.get('SCANNER_PROXY_HTTP')

#application_scanner = ZaproxyScanner(proxies={'http': 'http://zaproxy:8090', 'https': 'http://zaproxy:8090'})
application_scanner = ZaproxyScanner(proxies={'http': SCANNER_PROXY_HTTP, 'https': SCANNER_PROXY_HTTPS})
