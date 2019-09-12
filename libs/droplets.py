import os
import sys
import json
import logging
from var.vars import *

# Droplet high-level management.

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

    def __init__(self, name: str, region: str, size, image, ssh_keys: list,
                 backups: bool, ipv6: bool, user_data, private_networking: bool,
                 volumes: list, tags: list):
        self.name = name,
        self.region = region,
        self.size = size,

        # todo: type image
        self.image = image,
        self.ssh_keys = ssh_keys,
        self.backups = backups,
        self.ipv6 = ipv6,

        # todo: type user_data
        self.user_data = user_data,
        self.private_networking = private_networking,
        self.volumes = volumes,
        self.tags = tags,


class DropletManager(object):

    def __init__(self):
        self.managed_droplets = {}

    def add_droplet(self, droplet):
        pass

    def delete_droplet(self):
        pass

    def digital_ocean_delete_droplet(**kwargs):
        pass


if __name__ == '__main__':
    D = DropletManager()
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
