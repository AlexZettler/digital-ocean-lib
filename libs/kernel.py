import json
from dataclasses import dataclass, field


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
