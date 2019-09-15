import os
import sys
import json
import logging
import datetime as dt
from var.vars import *

from libs.image import Image
from libs.region import Region

from var.vars import *
from var.telemetry import do_requests

from dataclasses import dataclass, field

# Droplet high-level management

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)


@dataclass
class Kernel(object):
    id_: int
    name: str
    version: str

    @classmethod
    def from_json(cls, json_data: any):
        """
        This method is responsible for creating an instance from a string or dictionary representing the object.
        In the case of incorrect will cause an ____ Error.

        :param json_data: The data to convert to th instance
        :return: A Droplet instance
        """

        # Convert the json string top a dict if it is passed in this fashion
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        elif isinstance(json_data, dict):
            pass
        else:
            raise TypeError("The passed object must be either a string, or dictionary")

        id_ = json_data["id"]
        name = json_data["name"]
        version = json_data["version"]

        return cls(id_=id_, name=name, version=version)


@dataclass
class Droplet(object):
    id: int
    name: str
    memory: int  # The memory usage of the droplet in MegaBytes
    vcpus: int
    disk: int
    locked: bool
    created_at: dt.datetime
    status: str
    backup_ids: list
    snapshot_ids: list
    features: list
    region: Region
    image: Image
    size: dict
    size_slug: str
    networks: dict
    tags: list
    volume_ids: list

    kernel: Kernel = field(default=None)  # nullable
    next_backup_window: list = field(default_factory=list)  # nullable

    @classmethod
    def from_json(cls, json_data: any):
        """
        This method is responsible for creating an instance from a string or dictionary representing the object.
        In the case of incorrect will cause an ____ Error.


        :param json_data: The data to convert to th instance
        :return: A Droplet instance
        """

        # Convert the json string top a dict if it is passed in this fashion
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        elif isinstance(json_data, dict):
            pass
        else:
            raise TypeError("The passed object must be either a string, or dictionary")

        # Pull data from the droplet dictionary
        try:
            json_data: dict = json_data["droplet"]
        except KeyError as e:
            raise KeyError("the object must stem from the 'droplet' item")

        # todo: remove, these keys are for reference only
        keys_to_handle = ['id', 'name', 'memory', 'vcpus', 'disk', 'locked', 'status', 'kernel', 'created_at',
                          'features', 'backup_ids', 'snapshot_ids', 'image', 'volume_ids', 'size', 'size_slug',
                          'networks', 'region', 'tags']

        # Sanitize fields to ensure that all data is assigned properly
        try:
            _id: int = json_data["id"]
            name: str = json_data["name"]
            memory_mb: int = json_data["memory"]
            vcpus = int(json_data["vcpus"])
            disk: int = json_data["disk"]
            locked: bool = json_data["locked"]
            status: str = json_data["status"]

            kernel: Kernel = Kernel.from_json(json_data["kernel"])

            # Convert https://en.wikipedia.org/wiki/ISO_8601 time to a datetime object
            created_at: dt.datetime = dt.datetime.strptime(json_data["created_at"], "%Y-%m-%dT%H:%M:%SZ")

            features: list = json_data["features"]
            backup_ids: list = json_data["backup_ids"]
            snapshot_ids: list = json_data["snapshot_ids"]

            # todo: create json parser for image
            image: Image = json_data["image"]

            size_: dict = json_data["size"]
            size_slug: str = json_data["size_slug"]

            # todo: get more data for networks to parse and get more information
            networks: dict = json_data["networks"]

            # todo: create json parser for region
            region: Region = json_data["region"]

            tags: list = json_data["tags"]

            volume_ids: list = json_data["volume_ids"]

        except KeyError as e:
            raise e

        return cls(id=_id, name=name, memory=memory_mb, vcpus=vcpus, disk=disk, locked=locked, created_at=created_at,
                   status=status, kernel=kernel, backup_ids=backup_ids, snapshot_ids=snapshot_ids, features=features,
                   region=region, image=image, size=size_, size_slug=size_slug, networks=networks, tags=tags,
                   volume_ids=volume_ids)

    @classmethod
    def from_id(cls, id_: int):
        response = do_requests.digital_ocean_get_request(endpoint_url="/".join((DO_DROPLETS, str(id_))))
        return cls.from_json(response)

    @classmethod
    def create_new(cls, name: str, region_slug: str, size_slug: str, image: any,
                   ssh_keys: list = None, backups: bool = None, ipv6: bool = None, private_networking: bool = None,
                   user_data: str = None, monitoring: bool = None, volumes: list = None, tags: list = None):
        """

        :param name:
        :param region_slug:
        :param size_slug:
        :param image:
        :param ssh_keys:
        :param backups:
        :param ipv6:
        :param private_networking:
        :param user_data:
        :param monitoring:
        :param volumes:
        :param tags:
        :return:
        """

        if isinstance(image, int):
            pass
        elif isinstance(image, str):
            pass
        else:
            raise TypeError("The image param must reference either the image id integer, or the image slug string.")

        # todo: implement this method which will create a new digital-ocean droplet
        raise NotImplementedError

        # todo: receive the response object and return the parsed droplet
        return cls


class DropletManager(object):

    # todo: figure out the scope of this object, and weather is can be combined with the Droplet class

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
    k = Kernel(id_=10, name="test", version="v1.0")

    droplet_response_json = '''
    {
  "droplet": {
    "id": 3164494,
    "name": "example.com",
    "memory": 1024,
    "vcpus": 1,
    "disk": 25,
    "locked": false,
    "status": "active",
    "kernel": {
      "id": 2233,
      "name": "Ubuntu 14.04 x64 vmlinuz-3.13.0-37-generic",
      "version": "3.13.0-37-generic"
    },
    "created_at": "2014-11-14T16:36:31Z",
    "features": [
      "ipv6",
      "virtio"
    ],
    "backup_ids": [

    ],
    "snapshot_ids": [
      7938206
    ],
    "image": {
      "id": 6918990,
      "name": "14.04 x64",
      "distribution": "Ubuntu",
      "slug": "ubuntu-16-04-x64",
      "public": true,
      "regions": [
        "nyc1",
        "ams1",
        "sfo1",
        "nyc2",
        "ams2",
        "sgp1",
        "lon1",
        "nyc3",
        "ams3",
        "nyc3"
      ],
      "created_at": "2014-10-17T20:24:33Z",
      "type": "snapshot",
      "min_disk_size": 20,
      "size_gigabytes": 2.34
    },
    "volume_ids": [

    ],
    "size": {
    },
    "size_slug": "s-1vcpu-1gb",
    "networks": {
      "v4": [
        {
          "ip_address": "104.131.186.241",
          "netmask": "255.255.240.0",
          "gateway": "104.131.176.1",
          "type": "public"
        }
      ],
      "v6": [
        {
          "ip_address": "2604:A880:0800:0010:0000:0000:031D:2001",
          "netmask": 64,
          "gateway": "2604:A880:0800:0010:0000:0000:0000:0001",
          "type": "public"
        }
      ]
    },
    "region": {
      "name": "New York 3",
      "slug": "nyc3",
      "sizes": [
        "s-1vcpu-1gb",
        "s-1vcpu-2gb",
        "s-1vcpu-3gb",
        "s-2vcpu-2gb",
        "s-3vcpu-1gb",
        "s-2vcpu-4gb",
        "s-4vcpu-8gb",
        "s-6vcpu-16gb",
        "s-8vcpu-32gb",
        "s-12vcpu-48gb",
        "s-16vcpu-64gb",
        "s-20vcpu-96gb",
        "s-24vcpu-128gb",
        "s-32vcpu-192gb"
      ],
      "features": [
        "virtio",
        "private_networking",
        "backups",
        "ipv6",
        "metadata"
      ],
      "available": true
    },
    "tags": [

    ]
  }
}'''
    response_dict = json.loads(droplet_response_json)

    # print(response_dict.keys())

    # print(droplet_dict.keys())

    droplet = Droplet.from_json(droplet_response_json)

    print(droplet)

    # print(DropletManager.digital_ocean_create_droplet(
    #    name="bitshift_droplet", region="US_EAST", size="D23_X64", image="IMAGE", ssh_keys="ssgd34y3grsgbv",
    #    backups="yes", ipv6="no", user_data="testdata", private_networking="no", volumes="vol1", tags="this",
    # ))
