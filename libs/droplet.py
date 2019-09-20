import os
import sys
import json
import logging
import datetime as dt
from var.vars import *

from libs.image import Image
from libs.region import Region
from libs.size import Size
from libs.kernel import Kernel

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
    size: Size
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
            image: Image = Image(**json_data["image"])

            # Fuck size data inconsistancy
            try:
                size_: Size = Size(**json_data["size"])
            except TypeError:
                size_: Size = Size()

            size_slug: str = json_data["size_slug"]

            # todo: get more data for networks to parse and get more information
            networks: dict = json_data["networks"]

            # todo: create json parser for region
            region: Region = Region(**json_data["region"])

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
    pass
    # print(DropletManager.digital_ocean_create_droplet(
    #    name="bitshift_droplet", region="US_EAST", size="D23_X64", image="IMAGE", ssh_keys="ssgd34y3grsgbv",
    #    backups="yes", ipv6="no", user_data="testdata", private_networking="no", volumes="vol1", tags="this",
    # ))
