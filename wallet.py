import math
import random
import uuid

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from blockchain import *

class Key:
    def __init__(self):
        self.public = 0
        self.private = 0
    def __init__(self, public, private):
        self.public = public
        self.private = private

def generate_key_pair():
    # generate private/public key pair
    key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, \
        key_size=2048)
    # get public key in OpenSSH format
    public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, \
        serialization.PublicFormat.OpenSSH)
    # get private key in PEM container format
    private_key = key.private_bytes(encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption())

    return Key(public_key, private_key)

class Wallet:
    def __init__(self):
        self.key = generate_key_pair()

    def transfer(self, coins, reciever, chain):
        if not chain.is_chain_valid():
            quit("\nChain Invalid!!!\n\n")
    
        elif self.get_coins(chain) < coins:
            print("\nInsufficient Gotham Pixels!")
            quit("Process Terminated!!!\n\n")

        block = Block(Transaction(self.key.public, reciever, coins), chain.get_latest_block().hash)
        chain.add_block(block)
        return {"status":1, "msg":'success'}

    def get_coins(self, chain):
        sent = 0
        received = 0

        for i in range(len(chain.chain) - 1, -1, -1):
            trans = chain.chain[i].data
            if trans.sender == self.key.public:
                sent += trans.coins
            if trans.reciever == self.key.public:
                received+= trans.coins

        return received - sent

class Transaction:
    def __init__(self,public_key_sender, public_key_receiver, coins):
        self.sender = public_key_sender
        self.reciever = public_key_receiver
        self.id = uuid.uuid4()
        self.coins = coins