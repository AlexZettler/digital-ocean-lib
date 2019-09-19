
import os
import sys
import json
import logging
import requests
import random
import hashlib
from var.telemetry import DigitalOceanRequests
from libs.project import Project 
from var.telemetry import do_requests
from var.vars import *

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)
alt_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(os.environ['DO_AUTH']),
}

class Utilities():
    def random_number():
        random_num = os.urandom(16).encode('hex')
        return random_num

    def list_all_do_regions(self):
        try:
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_REGIONS)
            return r
        except requests.ConnectionError as e:
            logging.info("ERROR: Connection failed")
    def list_all_do_sizes(self):
        try:
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_SIZES)
            return r
        except requests.ConnectionError as e:
            logging.info("ERROR: Connection failed. {0}".format(e))
        except requests.exceptions.Timeout:
            logging.info("Error Connection timed out.")
    def list_all_do_droplets(self):
        try:
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_DROPLETS)
            return r
        except requests.ConnectionError as e:
            logging.info("ERROR: Connection failed.")
    def list_all_do_images(slef):
        try:
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_IAMGES)
            return r
        except requests.ConnectionError as e:
            logging.info("ERROR: Connection error")
            return -1, None
    def list_all_do_domains(slef):
        try:
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_DOMAINS)
            return r
        except requests.ConnectionError as re:
            logging.error("ERROR: Connection error")
            raise re
    def list_all_do_project_resources(slef, project_name):
        try:
            p = Project()
            ps = p.get_do_project_record(name="{}".format(project_name))
            if project_name in ps:
                project_id = ps['{}'.format(project_name)]
                r = do_requests.digital_ocean_get_request(endpoint_url=DO_PROJECTS + '/' + '{}'.format(project_id) + '/' + 'resources')
                return r
            elif project_name not in ps:
                logging.error("The project name specified is not valid.")
                return None
        except requests.ConnectionError:
            logging.error("Project name not specified.")
            return None
            
utils = Utilities()
print(utils.list_all_do_project_resources(project_name="brenden111"))

