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
        if data is None:
            return
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


print("\nTest 1 - Basic Test")
bc = BlockChain()
bc.add_block("cool")
print(bc)
#Block - hash(c34045c1a1db8d1b3fca8a692198466952daae07eaf6104b4c87ed3b55b6af1b) - data(cool) - prev_hash(0)
bc.add_block("neat")
print(bc)
# Block - hash(c34045c1a1db8d1b3fca8a692198466952daae07eaf6104b4c87ed3b55b6af1b) - data(cool) - prev_hash(0)
#Block - hash(60f858c0625d7b4100d5c5b260db766b653e600a54a492f7c9fad2157a226e91) - data(neat) - prev_hash(c34045c1a1db8d1b3fca8a692198466952daae07eaf6104b4c87ed3b55b6af1b)
bc.add_block("wow")
print(bc)
# Block - hash(c34045c1a1db8d1b3fca8a692198466952daae07eaf6104b4c87ed3b55b6af1b) - data(cool) - prev_hash(0)
# Block - hash(60f858c0625d7b4100d5c5b260db766b653e600a54a492f7c9fad2157a226e91) - data(neat) - prev_hash(c34045c1a1db8d1b3fca8a692198466952daae07eaf6104b4c87ed3b55b6af1b)
# Block - hash(b6dc933311bc2357cc5fc636a4dbe41a01b7a33b583d043a7f870f3440697e27) - data(wow) - prev_hash(60f858c0625d7b4100d5c5b260db766b653e600a54a492f7c9fad2157a226e91)

print("\nTest 2 - Empty Data")
bc = BlockChain()
bc.add_block("")
print(bc)
# Block - hash(e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855) - data() - prev_hash(0)

print("\nTest 3 - None Data")
bc = BlockChain()
bc.add_block(None)
print(bc)
# Doesn't print anything