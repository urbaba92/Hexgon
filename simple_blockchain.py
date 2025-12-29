import hashlib 
import time class Block:
    def __init__(self, index, 
    previous_hash, data, 
    timestamp, nonce=0):
        self.index = index 
        self.previous_hash = 
        previous_hash self.data 
        = data self.timestamp = 
        timestamp self.nonce = 
        nonce self.hash = 
        self.calculate_hash()
    def calculate_hash(self): 
        block_string = 
        f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}" 
        return 
        hashlib.sha256(block_string.encode()).hexdigest()
    def mine_block(self, 
    difficulty):
        target = "0" * 
        difficulty while 
        self.hash[:difficulty] 
        != target:
            self.nonce += 1 
            self.hash = 
            self.calculate_hash()
        print(f"Block mined: 
        {self.hash}")
class Blockchain: def 
    __init__(self, 
    difficulty=4):
        self.chain = 
        [self.create_genesis_block()] 
        self.difficulty = 
        difficulty
    def 
    create_genesis_block(self):
        return Block(0, "0", 
        "Genesis Block", 
        time.time())
    def get_latest_block(self): 
        return self.chain[-1]
    def add_block(self, data): 
        previous_block = 
        self.get_latest_block() 
        new_block = 
        Block(len(self.chain), 
        previous_block.hash, 
        data, time.time()) 
        new_block.mine_block(self.difficulty) 
        self.chain.append(new_block)
# Example usage
blockchain = 
Blockchain(difficulty=4) 
blockchain.add_block("First 
Block") 
blockchain.add_block("Second 
Block") for block in 
blockchain.chain:
    print(f"Block {block.index} [Hash: {block.hash}, Nonce: {block.nonce}]")
