import os
import sys
import json
import logging
from var.vars import *

#Droplet creation and deletetion

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
        droplet_json_payload = {}
        for arg in kwargs.values():
            droplet_json_payload
