from dataclasses import dataclass
import json


@dataclass
class Size(object):
    # note: All costs are measured in US dollars.

    slug: str  # A human-readable string that is used to uniquely identify each size.
    available: bool  # This is a boolean value that represents whether new Droplets can be created with this size

    # Amount of transfer bandwidth that is available for Droplets created in this size.
    # This only counts traffic on the public interface. The value is given in terabytes.
    transfer: float

    price_monthly: float  # The monthly cost of this Droplet size if the Droplet is kept for an entire month.
    price_hourly: float  # The price of the Droplet size as measured hourly. Measured in US dollars.
    memory: int  # The amount of RAM allocated to Droplets created of this size. The value is represented in megabytes.
    vcpus: int  # The integer of number CPUs allocated to Droplets of this size.
    disk: int  # The amount of disk space set aside for Droplets of this size. The value is represented in gigabytes.
    regions: list  # An array containing the region slugs where this size is available for Droplet creates.

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
            slug: str = json_data["slug"]
            available: bool = json_data["available"]
            transfer: float = json_data["transfer"]
            price_monthly: float = json_data["price_monthly"]
            price_hourly: float = json_data["price_hourly"]
            memory: int = json_data["memory"]
            vcpus: int = json_data["vcpus"]
            disk: int = json_data["disk"]
            regions: list = json_data["regions"]

        except KeyError as e:
            raise e

        return cls(slug=slug, available=available, transfer=transfer, price_monthly=price_monthly,
                   price_hourly=price_hourly, memory=memory, vcpus=vcpus, disk=disk, regions=regions)

    @classmethod
    def list_all(cls) -> list:
        pass
