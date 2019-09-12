
import os
import sys
import json
import logging
import requests
import random
import hashlib
from var.telemetry import DigitalOceanRequests
from var.vars import *

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)
alt_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % os.environ['DO_AUTH'],
}
request_object = DigitalOceanRequests(DO_BASE_URL, os.environ['DO_AUTH'])

class Utilities():
    def random_number():
        random_num = os.urandom(16).encode('hex')
        return random_num

    def list_all_do_regions(self):
        try:
            r = request_object.digital_ocean_get_endpoint(endpoint_url=DO_REGIONS)
            return r
        except requests.ConnectionError as e:
            logging.info("ERROR: Connection failed")
    def list_all_do_sizes(self):
        try:
            r = request_object.digital_ocean_get_endpoint(endpoint_url=DO_SIZES)
            return r
        except requests.ConnectionError as e:
            logging.info("ERROR: Connection failed. {0}".format(e))
        except requests.exceptions.Timeout:
            logging.info("Error Connection timed out.")
    def list_all_do_droplets(self):
        try:
            r = request_object.digital_ocean_get_endpoint(endpoint_url=DO_DROPLETS)
            return r
        except requests.ConnectionError as e:
            logging.info("ERROR: Connection failed.")
    def list_all_do_images(slef):
        try:
            r = request_object.digital_ocean_get_endpoint(endpoint_url=DO_IAMGES)
            return r
        except requests.ConnectionError as e:
            logging.info("ERROR: Connection error")
            return -1, None
    def list_all_do_domains(slef):
        try:
            r = request_object.digital_ocean_get_endpoint(endpoint_url=DO_DOMAINS)
            return r
        except requests.ConnectionError:
            logging.info("ERROR: Connection error")
            return -1, None
utils = Utilities()
print(utils.list_all_do_images())

