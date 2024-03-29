import time
from app.blockchain.block import Block


class Blockchain:
    # difficulty of our PoW algorithm
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_firts_block()

    def create_firts_block(self):
        firts_block = Block(0, [], time.time(), "0")
        firts_block.hash = firts_block.compute_hash()
        self.chain.append(firts_block)

    @property
    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        Why Do This Need Proof of Work? 
        Because they are decentralized and peer-to-peer by design, blockchains such as cryptocurrency networks require some way of achieving both consensus and security. 
        Proof of work is one such method that makes it too resource-intensive to try to overtake the network.
        """
        previous_hash = self.get_last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    def proof_of_work(self, block):
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof Of Work.
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.get_last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        self.unconfirmed_transactions = []
        return new_block.index
