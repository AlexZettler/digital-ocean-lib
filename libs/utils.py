
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
    def get_project_ids(self, **kwargs):
        try:
            j = 0
            r = request_object.digital_ocean_get_endpoint(endpoint_url=DO_PROJECTS)
            project_names = []
            for i in range(0, len(kwargs)):
                project_names += json.dumps(r['projects'][i]['name']).strip('"').split(',')
            for key, value in kwargs.items():
                if value in project_names:
                    project_payload = {
                        "ProjectName": "",
                        "ProjectID": "",
                    }
                    project_payload['ProjectName'] = value
                    project_payload['ProjectID'] = json.dumps(r['projects'][j]['id']).replace('"','')
                    j += 1
                elif (len(kwargs) <= 0):
                    logging.info("Additional arguments required.")
                    return -1, None
                else:
                    logging.debug("Project(s) does not exist")
                    return -1, None
            return project_payload
        except requests.ConnectionError:
            logging.info("ERROR: Connection error")
            return -1, None
        except json.JSONDecodeError:
            logging.info("JSONDecode error.")
            return -1, None
    def create_do_project(self, **kwargs):
        json_payload_template = {
            "name": "",
            "description": "",
            "purpose": "",
            "environment": ""
        }
        for key, value in kwargs.items():
            json_payload_template[key] = value
        payload_str = json.dumps(json_payload_template).replace('\'', '"')
        print(payload_str)
        try:
            r = request_object.digital_ocean_post_endpoint(payload_str, endpoint_url=DO_PROJECTS)
            return r
        except requests.exceptions.ConnectionError as ce:
            logging.info("Connection error!")
        return json_payload_template
    #def delete_do_project(slef, project_id):
utils = Utilities()
print(utils.get_project_ids(name0="brenden111", name1="Cool project", name3="Second project"))
'''
print(utils.create_do_project(
    name="Cool project",
    description="This is going to be used as a test project",
    purpose="Service or API",
    environment="Development",
))
'''
