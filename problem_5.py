import hashlib, time

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def calc_hash(self, data: str) -> str:
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def _create_block(self, data: str, prev_hash: str) -> Block:
        return Block(time.gmtime(), data, prev_hash)

    def add_block(self, data: str):
        if self.head is None:
            block = self._create_block(data, "0")
            self.head = block
            self.tail = block
            return
        self.tail.next = self._create_block(data, self.tail.hash)
        self.tail = self.tail.next
        return
    
    def __str__(self):
        s = ""
        block = self.head
        while block is not None:
            s += f"Block - hash({block.hash}) - data({block.data}) - prev_hash({block.previous_hash})\n"
            block = block.next
        return s


# # Uncomment to see in action
# bc = BlockChain()
# bc.add_block("cool")
# print(bc)
# bc.add_block("neat")
# print(bc)
# bc.add_block("wow")
# print(bc)