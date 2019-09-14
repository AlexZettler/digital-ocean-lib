class Region(object):
    """
    This class describes the Region object
    """

    def __init__(self, slug: str, name: str, sizes: list, available: bool, features: bool):
        slug: str = slug
        name: str = name
        sizes: list = sizes
        available: bool = available
        features: list = features

    @staticmethod
    def get_all_regions() -> list:
        """
        :return: A list of all regions
        """
        # todo: implement
        # https://developers.digitalocean.com/documentation/v2/#list-all-regions
        raise NotImplementedError

    @staticmethod
    def get_available_regions():
        return [r for r in Region.get_all_regions() if r.available]
