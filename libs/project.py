import os
import sys
import json
import logging
import requests
import random
import hashlib
from itertools import chain
from var.telemetry import DigitalOceanRequests, do_requests
from var.vars import *

# Project management.

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)


# alt_headers = {
#            "Content-Type": "application/json",
#            "Authorization": "Bearer %s" % os.environ['DO_AUTH'],
# }
# request_object = DigitalOceanRequests(DO_BASE_URL, os.environ['DO_AUTH'])

#Lot's of debugging and testing still required for get_project_ids

class Project(object):
    def get_project_ids(self, **kwargs):
        try:
            j = 0
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_PROJECTS)
            project_names = []
            project_payload = {}
            data_final ={}
            for i in range(0, len(kwargs)):
                project_names += json.dumps(r['projects'][i]['name']).strip('"').split(',')
            #print(project_names)
            for key, value in kwargs.items():
                print(value)
                if value in project_names:
                    project_payload['ProjectName'] = value
                    project_payload['ProjectID'] = json.dumps(r['projects'][j]['id']).replace('"', '')
                    data_final.update({project_payload['ProjectName']:project_payload['ProjectID']})
                elif len(kwargs) <= 0:
                    logging.info("Additional arguments required.")
                    return -1, None
                else:
                    logging.error("Project(s) does not exist - Please ensure name is spelt correctly.")
                    return -1, None
            logging.info("SUCCESS: Returning project names and IDs")
            return data_final
        except requests.ConnectionError:
            logging.info("ERROR: Connection error")
            return -1, None
        except TypeError:
            logging.info("Cannot serialize the object.")
            return -1, None

    def create_do_project(self, **kwargs):

        #Todo: Purpose and environment are pre-defined fields - verfiy these are correct.

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
            r = do_requests.digital_ocean_post_endpoint(payload_str, endpoint_url=DO_PROJECTS)
            return r
        except requests.exceptions.ConnectionError as ce:
            logging.info("Connection error!")
        return json_payload_template

#'''
    def delete_do_project(self, project_name):
        try:
            if project_name in self.get_project_ids(name=project_name):
                print(self.get_project_ids(name=project_name))
            #r = do_requests.digital_ocean_delete_request(endpoint_url=DO_PROJECTS, project_id)
            return 1
        except requests.exceptions.ConnectionError as ce:
            logging.info
#'''

if __name__ == '__main__':
    project = Project()
    print(project.get_project_ids(name1="Cool project"))
    #rint(project.delete_do_project("Second project"))
    '''
    print(utils.create_do_project(
        name="Cool project",
        description="This is going to be used as a test project",
        purpose="Service or API",
        environment="Development",
    ))
    '''
