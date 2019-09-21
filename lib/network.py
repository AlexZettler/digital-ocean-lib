# *** Domain realted methods *** 
import os
import base64
import json
import requests
import logging
import socket
import dns.resolver
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES
from var.telemetry import do_requests
from var.vars import DO_DOMAINS

name_servers = [
   b'B5jvm2XLeLrMFTmSHkRN5N8vUBAxgerGCjz9tJ4erhHxtMgeLRH75rXuh4X4OndN',
   b'H9OUwDUe1RgOLokV2lJ+FgycaLS+sRCribNU5e7lH+GXMHazMuwcJTQ7DpnHh6cw',
   b'uT4W+2QxoSb4oHEiZvDy/tC9u1xX1TZVBL0TdzTQ7FWBDrfq026fl6etfpQaGXKd',
]
class Domain:
    def __init__(self):
        self.FRAME_BUFFER = 65536
        self.OS_NAME = os.name
    # *** Domain methodhere ***
    domain_record_types = [
        'A', #IPv4 Host
        'AAAA', #IPv6 Host
        'CAA', #Certificate Authority restrictor
        'CNAME', #Alias for canonical hostname
        'MX', #Mail exchanges
        'NS', #Name servers
        'TXT', #Associate a string of text with a host
        'SRV', #Location and port number of servers - for specific purposes
        'SOA' #Administrative information about the zone
    ]

    #Provisional function -> Will be replaced by stream collection : Will have to migrate to web server
    ''' *** LOCAL VERSION OF METHOD *** '''
    def get_eframe(self, PORT_NUMBER):
        try:
            HOST = socket.gethostbyname(socket.gethostname())
            _connection = socket.socket(
                socket.AddressFamily.AF_INET, 
                socket.SOCK_RAW, 
                socket.IPPROTO_IP
            )
            _connection.bind((HOST, 0))
            socket_packet_options = _connection.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            #_connections.ioctl -> (Input/output control): Here we tell the socket to receive all IPv4.v6 packets through an interface
            #in this case loopback.
            ''' https://docs.microsoft.com/en-us/previous-versions/windows/desktop/legacy/ee309610(v%3Dvs.85) '''
            if self.OS_NAME == 'NT':
                sock_on_ipv4 = _connection.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
                frame = _connection.recvfrom(self.FRAME_BUFFER)
                sock_off_ipv4 = _connection.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
                return frame
            else:
                frame = _connection.recvfrom(self.FRAME_BUFFER)
                return frame
        except OSError as ose:
            raise ose
        
    def get_do_domain(self, domain_name):
        try:
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_DOMAINS +  '/' +  domain_name)
            if  len(r) <=3  or r['id']=='not_found':
                logging.info(r)
                return None
            else:
                return r
        except requests.ConnectionError as error:
            raise error
    def list_all_do_domain_records(self):
        try:
            r = do_requests.digital_ocean_get_request(endpoint_url=DO_DOMAINS)
            if  len(r) <=3  or r['id']=='not_found':
                logging.info(r)
                return None
            else:
                return r
        except requests.ConnectionError as error:
            raise error
D = Domain()
#print(D.list_all_do_domain_records())
print(D.get_eframe(PORT_NUMBER=0))
