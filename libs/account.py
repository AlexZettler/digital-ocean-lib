import os
import sys
import requests
import json
import logging
from var.telemetry import DigitalOceanRequests, do_requests
from var.vars import *

# For account specific calls.

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)

# DO_BASE_URL = "https://api.digitalocean.com"
# DO_ACCOUNT = "/v2/account"
req_object = do_requests  # DigitalOceanRequests(DO_BASE_URL, os.environ['DO_AUTH'])


class Account(object):
    def check_account_status(self, url_endpoint):
        response_data = {}
        r = req_object.digital_ocean_get_endpoint(DO_ACCOUNT)
        response_data['status'] = json.dumps(r['account']['status']).replace('"', '')
        return response_data['status']

    def get_account_info(self, url_endpoint):
        json_response = {}
        account_info = req_object.digital_ocean_get_endpoint(DO_ACCOUNT)
        for key in account_info:
            json_response[key] = json.dumps(account_info[key]).replace('"', '')
        return json_response


if __name__ == '__main__':
    a_info = Account()
    print(a_info.check_account_status(DO_ACCOUNT))
