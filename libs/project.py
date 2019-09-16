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

class Project(object):
    def get_project_ids(self, **kwargs):
        project_names = []
        project_payload = {}
        data_final = {}
        try:
            j = 0
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_PROJECTS)
            for i in range(0, len(r['projects'])):
                project_names += json.dumps(r['projects'][i]['name']).strip('"').split(',')
            for key, value in kwargs.items():
                if value in project_names:
                    project_payload['ProjectName'] = value
                    project_payload['ProjectID'] = json.dumps(r['projects'][j]['id']).replace('"', '')
                    data_final.update({project_payload['ProjectName']:project_payload['ProjectID']})
                else:
                    logging.error("Project(s) does not exist - Please ensure name is spelt correctly.")
                    return -1, None
            logging.info("SUCCESS: Returning project names and IDs")
            return data_final
        except requests.ConnectionError:
            logging.info("ERROR: Connection error")
            return -1, None
        except TypeError:
            logging.error("Cannot serialize the object.")
            return -1, None

    def create_do_project(self, **kwargs):

        #Todo: Purpose and environment are pre-defined fields - verfiy these are correct.
        #Todo: Create allowed_envs = ["Development" , "Staging", "Production"]
        '''
        #Todo: Create allowed_purposes = [
        # "Just trying out DigitalOcean" , 
        # "Class project / Educational purposes" ,
        # "Website or blog" , 
        # "Web Application" ,
        # "Service or API" ,
        # "Mobile Application" ,
        # "Machine learning / AI / Data processing" ,
        # "IoT"] ,
        # "Operational / Developer tooling"
        ]  
        '''

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
            logging.info("Connection failed")
            raise ce
        return json_payload_template

    def delete_do_project(self, project_name):
        try:
            #We will verify the droplet exists first.
            project_obj = self.get_project_ids(name=project_name)
            if project_name in project_obj:
                p_id = project_obj['{}'.format(project_name)]
                r = do_requests.digital_ocean_delete_request(endpoint_url=DO_PROJECTS, unique_id=p_id)
                return r
            elif project_name not in project_obj:
                logging.error("The project name specified is not valid.")
                return None
        except requests.exceptions.ConnectionError as ce:
            logging.error("Connection Failed")
            raise ce

    def get_do_default_project():
        try:
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_PROJECTS + '/' + 'default')
            return r
        except requests.ConnectionError as ce:
            logging.error("Connection failed")
            raise ce

if __name__ == '__main__':
    #All of the projects being passed into these functions are currently test examples. 

    project = Project()
    #print(project.get_project_ids(name1="Cool project"))
    #print(project.delete_do_project("Second project"))
    print(project.get_do_default_project())
    
    '''
    print(utils.create_do_project(
        name="Cool project",
        description="This is going to be used as a test project",
        purpose="Service or API",
        environment="Development",
    ))
    '''
