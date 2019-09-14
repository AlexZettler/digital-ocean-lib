from libs.region import Region
import datetime as dt


class Image(object):
    """
    This class describes an image object
    """

    # https://developers.digitalocean.com/documentation/v2/#images

    def __init__(self, id_: int, slug: str,
                 name: str, type_: str,
                 distribution: str,
                 public: bool,
                 regions: list,
                 created_at: object,
                 min_disk_size: int,
                 size_gigabytes: float,
                 description: str,
                 tags: list,
                 status: str,
                 error_message: str):

        #  A slug is a unique str that can be used to reference a d-o public image instead of an id
        self.id_: int = id_
        self.slug: str = slug

        # A human readable name given to the image
        self.name: str = name

        # The kind of image, describing the duration of how long the image is stored.
        # This is either "snapshot", "backup", or "custom".
        self.type_: str = type_

        # This attribute describes the base distribution used for this image. For custom images, this is user defined.
        self.distribution: str = distribution

        # This is a boolean value that indicates whether the image in question is public or not.
        # An image that is public is available to all accounts. A non-public image is only accessible from your account.
        self.public: bool = public

        # This attribute is an array of the regions that the image is available in.
        # The regions are represented by their identifying slug values.
        self.regions: list = regions

        # Creates a created_at datetime attribute from either a string or datetime object.
        if isinstance(created_at, str):
            self.created_at: dt.datetime = dt.datetime.fromisoformat(created_at)
        elif isinstance(created_at, dt.datetime):
            self.created_at: dt.datetime = created_at
        else:
            raise TypeError(f"The created_at string could not be parsed: '{created_at}'")

        # The minimum disk size in GB required for a Droplet to use this image.
        self.min_disk_size: int = min_disk_size

        # The size of the image in gigabytes.
        self.size_gigabytes: float = size_gigabytes

        # An optional free-form text field to describe an image.
        self.description: str = description

        # An array containing the names of the tags the image has been tagged with.
        self.tags: list = tags

        # A status string indicating the state of a custom image.
        # This may be "NEW", "available", "pending", or "deleted".
        self.status: str = status

        # A string containing information about errors that may occur when importing a custom image.
        self.error_message: str = error_message

    @classmethod
    def list_account_images(cls) -> list:
        # todo: implement
        # https://developers.digitalocean.com/documentation/v2/#list-all-images
        raise NotImplementedError
        images = []
        return images

    def from_json(self, json_str: str):
        pass
