import os
import sys
import requests
import json
import logging
from var.telemetry import DigitalOceanRequests

#For account specific calls.
#

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)

DO_BASE_URL = "https://api.digitalocean.com"
DO_ACCOUNT = "/v2/account"
req_object = DigitalOceanRequests(DO_BASE_URL, os.environ['DO_AUTH'])

class Account():
    def get_account_info(self, url_endpoint):
        json_response = {}
        try:
            account_info = req_object.digital_ocean_get_endpoint(DO_ACCOUNT)
            for key in account_info:
                json_response[key] = json.dumps(account_info[key]).replace('"','')
            return
        except requests.exceptions.ConnectionError as re:
            logging.info("Error request timed out! /{0}/".format(re))
            return -1, None
        except requests.exceptions.TooManyRedirects:
            logging.info("Bad URL")
            return None, -1
a_info = Account()
print(a_info.get_account_info(DO_ACCOUNT))

        




