
import os
import sys
import json
import logging
import requests
from var.telemetry import DigitalOceanRequests
from var.vars import DO_REGIONS, DO_BASE_URL, DO_SIZES, DO_DROPLETS, DO_IAMGES

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
            logging.info("ERROR: Connection failed.")
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
    def create_do_project(self, **kwargs):
        json_payload_template = {
            "name": "",
            "description": "",
            "purpose": "",
            "environment": ""
        }
        for key, value in kwargs.items():
            json_payload_template[key] = value
        return json_payload_template
    def delete_do_projecy(slef, project_id):

regions = Utilities()
print(regions.list_all_do_regions())
