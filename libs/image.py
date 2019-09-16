from dataclasses import dataclass
import json

from libs.region import Region
import datetime as dt

from dataclasses import dataclass, field

from var.vars import *
from var.telemetry import do_requests


@dataclass
class Image(object):
    """
    This class describes an image object
    """

    # https://developers.digitalocean.com/documentation/v2/#images

    # Optional args: 'description', 'tags', 'status', and 'error_message'

    id: int
    slug: str
    name: str
    type: str
    distribution: str
    public: bool
    regions: list
    created_at: dt.datetime
    min_disk_size: int
    size_gigabytes: float
    tags: list = field(default_factory=list)
    description: str = field(default="")
    status: str = field(default="")
    error_message: str = field(default="")

    @classmethod
    def list_images(cls) -> list:
        # todo: implement
        # https://developers.digitalocean.com/documentation/v2/#list-all-images
        raise NotImplementedError
        images = list()
        return images

    @classmethod
    def from_json(cls, json_data: any):
        """
        This method is responsible for creating an instance from a string or dictionary representing the object.
        In the case of incorrect will cause an ____ Error.

        :param json_data: The data to convert to th instance
        :return: An Image instance
        """

        # Convert the json string top a dict if it is passed in this fashion
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        elif isinstance(json_data, dict):
            pass
        else:
            raise TypeError("The passed object must be either a string, or dictionary")

        id_: int = json_data["id"]
        slug: str = json_data["slug"]
        name: str = json_data["name"]
        type_: str = json_data["type"]
        distribution: str = json_data["distribution"]
        public: bool = json_data["public"]
        regions: list = json_data["regions"]
        created_at: dt.datetime = dt.datetime.strptime(json_data["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        min_disk_size: int = json_data["min_disk_size"]
        size_gigabytes: float = json_data["size_gigabytes"]
        description: str = json_data["description"]
        tags: list = json_data["tags"]
        status: str = json_data["status"]
        error_message: str = json_data["error_message"]

        return cls(id_, slug, name, type_, distribution, public, regions, created_at, min_disk_size, size_gigabytes,
                   description, tags, status, error_message)
