import os
import requests 
import json
import logging

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)
alt_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % os.environ['DO_AUTH'],
}
class DigitalOceanRequests():
    def __init__(self, do_base_url, do_auth_key):
        self.do_base_url = "https://api.digitalocean.com"
        self.do_auth_key = os.environ['DO_AUTH']
        self.master_str = '{0}/{1}/{2}'.format(self.do_base_url, self.do_auth_key, 'HTTPS').replace('"','')

    def digital_ocean_get_endpoint(self, endpoint_url):
        json_response = {}
        try:
            get_request = requests.get(url=self.do_base_url + endpoint_url, headers=alt_headers).json()
            return get_request
        except requests.ConnectionError as exception:
            logging.error(exception)
            return -1, None

    def digital_ocean_post_endpoint(self, do_payload, endpoint_url):
        json_response = {}
        try:
            post_request = requests.post(url=self.do_base_url + endpoint_url, headers=alt_headers, data=do_payload).json()
        except requests.ConnectionError as exception:
            logging.error(exception)
            return 
d = DigitalOceanRequests("","")
print(d.digital_ocean_get_endpoint("/v2/volumes"))

        