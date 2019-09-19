import os
import sys
import json
import logging
from var.vars import *
from libs.utils import Utilities

#Droplet high-level management.

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)
alt_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % os.environ['DO_AUTH'],
}
utils = Utilities()

class Droplets():
    def digital_ocean_create_droplet(**kwargs):
        droplet_json_payload_template = {
            "name": "",
            "region": "",
            "size": "",
            "image": "",
            "ssh_keys": [
                ""
            ],
            "backups": "",
            "ipv6": "",
            "user_data": "",
            "private_networking": "",
            "volumes": "",
            "tags": [
                ""
            ]
        }
        for key, value in kwargs.items():
            droplet_json_payload[key] = value
        return droplet_json_payload_template
    #def digital_ocean_delete_droplet(self, droplet_id):
D = Droplets()
print(Droplets.digital_ocean_create_droplet(
    name="bitshift_droplet", 
    region="US_EAST", 
    size="D23_X64",
    image="IMAGE",
    ssh_keys="ssgd34y3grsgbv",
    backups="yes",
    ipv6="no",
    user_data="testdata",
    prviate_networking="no",
    volumes="vol1",
    tags="this",
))
