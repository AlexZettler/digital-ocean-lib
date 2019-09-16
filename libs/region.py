from dataclasses import dataclass
import json

from var.vars import *
from var.telemetry import do_requests


@dataclass
class Region(object):
    """
    This class describes the Region object
    """
    slug: str
    name: str
    sizes: list
    available: bool
    features: list

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

        slug: str = json_data["slug"]
        name: str = json_data["name"]
        sizes: list = json_data["sizes"]
        available: bool = json_data["available"]
        features: list = json_data["features"]

        return cls(slug, name, sizes, available, features)

    @staticmethod
    def get_regions() -> list:
        """
        :return: A list of all regions
        """
        # todo: implement
        # https://developers.digitalocean.com/documentation/v2/#list-all-regions
        raise NotImplementedError

    @staticmethod
    def get_available_regions():
        return [r for r in Region.get_all_regions() if r.available]
