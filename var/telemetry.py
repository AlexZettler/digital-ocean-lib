import os
import requests
import json
import logging

# This file handles HTTP Request methods.
# Still needing to test these functionalities.

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)
alt_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(os.environ['DO_AUTH'])
}

class DigitalOceanRequests(object):
    def __init__(self):
        self.do_base_url = "https://api.digitalocean.com"
        self.do_auth_key = os.environ['DO_AUTH']
        self.master_str = '{0}/{1}/{2}'.format(self.do_base_url, self.do_auth_key, 'HTTPS').replace('"', '')

    def digital_ocean_get_request(self, endpoint_url):
        json_response = {}
        try:
            print(os.environ['DO_AUTH'])
            get_request = requests.get(url=self.do_base_url + endpoint_url, headers=alt_headers).json()
            return get_request
        except requests.ConnectionError as exception:
            logging.error(exception)
            return -1, None

    def digital_ocean_post_request(self, do_payload, endpoint_url):
        json_response = {}
        try:
            post_request = requests.post(url=self.do_base_url + endpoint_url, headers=alt_headers,
                                         data=do_payload).json()
            return post_request
        except requests.ConnectionError as exception:
            logging.error(exception)
            return -1, None

    def digital_ocean_delete_request(self, endpoint_url, unique_id):
        json_response = {}
        try:
            delete_request = requests.delete(url=self.do_base_url + endpoint_url + '/' + unique_id, headers=alt_headers).json()
            print(self.do_base_url + endpoint_url + '/' + unique_id)
            return delete_request
        except requests.ConnectionError as exception:
            logging.error(exception)
            return -1, None

    def digital_ocean_put_request(self, endpoint_url, unique_id):
        json_response = {}
        try: 
            put_request = requests.put(self, url=self.do_base_url + endpoint_url + unique_id).json()
            return put_request
        except requests.ConnectionError as exception:
            logging.error(exception)
            return -1, None
do_requests = DigitalOceanRequests()
print(do_requests.digital_ocean_get_request("/v2/account"))
if __name__ == '__main__':
    pass
