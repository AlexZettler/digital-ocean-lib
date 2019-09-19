# *** Domain realted methods *** 
import os
import base64
import json
import dns.resolver
from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES

name_servers = [
   b'B5jvm2XLeLrMFTmSHkRN5N8vUBAxgerGCjz9tJ4erhHxtMgeLRH75rXuh4X4OndN',
   b'H9OUwDUe1RgOLokV2lJ+FgycaLS+sRCribNU5e7lH+GXMHazMuwcJTQ7DpnHh6cw',
   b'uT4W+2QxoSb4oHEiZvDy/tC9u1xX1TZVBL0TdzTQ7FWBDrfq026fl6etfpQaGXKd',
]
class Domain:
    # *** Domain methodhere ***

block_size = 16
pad = lambda s: bytes(s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size), 'utf-8')
unpad = lambda s : s[0:-ord(s[-1:])]


#Sample Encryption method
#Source: https://www.novixys.com/blog/using-aes-encryption-decryption-python-pycrypto/
''' *** TODO : Lean more avout AES 256 - Encryption ****'''

class AESCipher:
    def __init__(self, key):
        #Key has to be converted to bytes sized object.
        self.key =  bytes(key, 'utf-8')

    def encrypt(self, raw):
        raw = pad(raw)
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
    
