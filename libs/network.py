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
            sock_options = _connection.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
            frame = _connection.recvfrom(65565)
            _connection.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            return frame
    def frame_deconstruction(self, frame):
        pass

        except (OSError, socket.error) as ce:
            raise ce
            return -1, None 
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

'''
We introduce paddding to ensure the blocksize containing the data
conforms to that specified by AES - AES Has a fixed block size.
In the event that raw_data < AESBlockSize we pad the remaining to
fit inside of the block.

'''

block_size = 16
pad = lambda s: bytes(s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]


#Sample Encryption method
#Source: https://www.novixys.com/blog/using-aes-encryption-decryption-python-pycrypto/
''' *** TODO : Lean more avout AES 256 - Encryption ****'''

class AESCipher:
    def __init__(self, key):
        #Key has to be converted to bytes sized object.
        #bytes -> Converts object into bytes object.
        self.key =  bytes(key, 'utf-8')

    def encrypt(self, raw):
        raw = pad(raw)
        #IV : Initialization vector
        iv = Random.new().read( AES.block_size )
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode('utf8')

cipher = AESCipher(os.environ['TOKEN_KEY'])
for i in range (0, len(name_servers)):
    decrypted = cipher.decrypt(name_servers[i])
D = Domain()
#print(D.list_all_do_domain_records())
print(D.get_eframe(PORT_NUMBER=0))
