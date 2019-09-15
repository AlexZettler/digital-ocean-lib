from dataclasses import dataclass
import json

from libs.region import Region
import datetime as dt

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
