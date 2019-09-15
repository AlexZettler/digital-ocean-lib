import os
import sys
import json
import logging
import datetime as dt
from var.vars import *

from libs.image import Image
from libs.region import Region

# Droplet high-level management

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)
alt_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer %s" % os.environ['DO_AUTH'],
}

class Droplet(object):
    droplet_json_payload_template = {
        "id": "",
        "name": "",
        "region": "",
        "size": "",
        "image": "",
        "ssh_keys": [""],
        "backups": "",
        "ipv6": "",
        "user_data": "",
        "private_networking": "",
        "volumes": "",
        "tags": [""],
    }

    def __init__(self, name: str, region: Region, size, image, ssh_keys: list,
                 backups: bool, ipv6: bool, user_data, private_networking: bool,
                 volumes: list, tags: list):
        self.name = name,
        self.region: Region = region,
        self.size = size,

        # todo: type image
        self.image: Image = image,
        self.ssh_keys: list = ssh_keys,
        self.backups: bool = backups,
        self.ipv6: bool = ipv6,

        # todo: type user_data
        self.user_data = user_data,
        self.private_networking = private_networking,
        self.volumes = volumes,
        self.tags = tags,

    @classmethod
    def from_json(cls, json_str: str):
        json_data: dict = json.loads(json_str)

        # Verifies that keys in the template are found in the json object
        if not set(*json_data.keys()).issubset(set(*cls.droplet_json_payload_template.keys())):
            raise IndexError("The keys of the json object do not match the template.")

        # Sanitize fields to ensure that all data is assigned properly
        try:
            name = json_data["name"]
            region = json_data["region"]
            size = json_data["name"]
            image = json_data["name"]
            ssh_keys = json_data["name"]
            backups: bool = json_data["name"] == "yes"
            ipv6: bool = json_data["ipv6"] == "yes"

            user_data = json_data["user_data"]
            private_networking: bool = json_data["private_networking"]
            volumes: list = json_data["volumes"]
            tags: list = json_data["tags"]

        except KeyError as e:
            raise e

        return cls(name="", region=None, size="", image="", ssh_keys=[],
                   backups=True, ipv6=False, user_data="", private_networking=True,
                   volumes=[], tags=[])


class DropletManager(object):

    def __init__(self):
        self.managed_droplets = {}

    # https://developers.digitalocean.com/documentation/v2/#list-all-droplets
    def get_all_droplets(self):
        raise NotImplementedError

    def add_droplet(self, droplet):
        raise NotImplementedError

    def delete_droplet(self, droplet_id: int):
        raise NotImplementedError


if __name__ == '__main__':
    D = DropletManager()
    #Test data

    print(DropletManager.digital_ocean_create_droplet(
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
