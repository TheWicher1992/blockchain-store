import hashlib
from datetime import datetime
import time


class Block:
    # The constructor initializes all the components of a block
    def __init__(self, data, previous_block_hash=''):
        # Timestamps add a factor of verification when checking a block's validity
        self.timestamp = datetime.now().strftime("%d/%m/%Y")
        self.nonce = 0  # This adds randomization to the mix when the block is mined
        self.data = data
        self.previous_block_hash = previous_block_hash
        self.hash = self.calculate_hash()

    # Returns the SHA256 hash of a concatenated string containing the nonce, timestamp, data and previous block's hash (in the same order). Remember to encoded
    # the string before hashing it!
    def calculate_hash(self):
        sha256 = hashlib.sha256()
        sha256.update(str.encode(str(self.nonce)))
        sha256.update(str.encode(str(self.timestamp)))
        sha256.update(str.encode(str(self.data)))
        sha256.update(str.encode(str(self.previous_block_hash)))
        return int(sha256.hexdigest(), 16)

    # Requires a miner to provide a proof of work before they could modify the blockchain
    def mine_block(self, difficulty):
        mask_len = 256 - difficulty
        new_hash = self.calculate_hash()
        while(not (new_hash >> mask_len == 0)):
            self.nonce += 1
            new_hash = self.calculate_hash()
        self.hash = new_hash
        pass


class Blockchain:
    # The constructor initializes a chain containing just the genesis block
    def __init__(self, difficulty, genesis_block_data):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block(genesis_block_data)]

    # Initializes and returns the first block in a chain
    def create_genesis_block(self, data):
        return Block(data=data, previous_block_hash='')
        pass

    # Adds a new block to the end of the chain. Remember blocks need to be mined before they can be added!
    def add_block(self, block):
        block.mine_block(self.difficulty)
        self.chain.append(block)
        pass

    # Returns the block that was most recently added
    def get_latest_block(self):
        return self.chain[-1]
        pass

    # Returns a bool which indicates whether the chain is still valid or have been tampered with
    def is_chain_valid(self):
        for i in range(len(self.chain) - 1, 0, -1):
            this_block = self.chain[i]
            prev_block = self.chain[i-1]
            this_block_hash_check = this_block.calculate_hash() == this_block.hash
            if(not this_block_hash_check):
                return False
            prev_block_hash_check = this_block.previous_block_hash == prev_block.calculate_hash()
            if(not prev_block_hash_check):
                return False
        return True

    # Prints the data and hashes of each block in the chain

    def print_chain(self):
        print("----------------------------Gotham Blockchain----------------------------")
        for block in self.chain:
            if block.data.sender == '':
                block.data.sender = "Genesis Block! Hence no sender available."
            print("\nID: " + str(block.data.id),"\nSender Public Key: " + str(block.data.sender)[0:50]+"...........", "\nReceiver Public Key: " + str(block.data.reciever)[0:50]+"...........", "\nGotham Pixels Transferred: " + str(block.data.coins)+"\n")
        print("\n\n")