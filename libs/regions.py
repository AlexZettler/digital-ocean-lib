
import os
import sys
import json
import logging
import requests
from var.telemetry import DigitalOceanRequests
from var.vars import DO_REGIONS, DO_BASE_URL

#Droplet creation and deletetion

logging.basicConfig(
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    level=logging.INFO,
)
alt_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer %s" % os.environ['DO_AUTH'],
}
request_object = DigitalOceanRequests(DO_BASE_URL, os.environ['DO_AUTH'])

class Regions():
    def list_all_do_regions(self):
        r = request_object.digital_ocean_get_endpoint(endpoint_url=DO_REGIONS)
        return r
regions = Regions()
print(regions.list_all_do_regions())
