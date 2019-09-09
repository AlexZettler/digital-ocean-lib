import os
import sys
import json
import logging
from var.vars import *

#Droplet creation and deletetion...s

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)
alt_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % self.do_auth_key,
}
class Droplets():
    def digital_ocean_create_droplet(**kwargs):
        droplet_json_payload = {
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
        return droplet_json_payload['name']
D = Droplets()
print(D.digital_ocean_create_droplet("THIs","That","Yes"))
