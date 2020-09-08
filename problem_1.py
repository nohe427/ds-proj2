class Node(object):
    def __init__(self, key:int=None, value:int=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity:int):
        # Initialize class variables
        self.itemsD = {}
        self.size = 0
        self.capacity = self._set_capacity(capacity)
        self.head = None
        self.tail = None

    # Setting min capacity to 1. Otherwise the cache doesn't work at all.
    def _set_capacity(self, value: int) -> int:
        if value < 1:
            return 1
        return value

    def get(self, key: int) -> int:
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.size == 0:
            return -1
        if key not in self.itemsD:
            return -1
        node = self.itemsD[key]
        self._remove_node(node)
        self._make_node_head(node)
        return node.value

    def set(self, key: int, value: int) -> None:
        if key is None: # We can but probably should not use a None type key
            return
        # Set the value if the key is not present in the cache.
        node = Node(key, value)
        if self.head == None:
            self.size += 1
            self.head = node
            self.tail = node
            self.itemsD[key] = node
            return
        if self._already_exists(node):
            # No need to move the head if its the same
            if self.head.key == node.key:
                self.head.value = node.value
                return
            else:
                self._remove_node(node)
                self._make_node_head(node)
                return
        else:
            self._make_node_head(node)

        # If the cache is at capacity remove the oldest item. 
        if self._at_capacity():
            self._remove_oldest()
        else:
            self.size += 1

    def _make_node_head(self, node:Node) -> None:
        node.next = self.head
        self.head = node
        node.next.prev = node
        self.itemsD[node.key] = node

    def _already_exists(self, node: Node) -> bool:
        return node.key in self.itemsD

    def _remove_node(self, node:Node) -> None:
        remove_me = self.itemsD[node.key]
        # We are at the tail
        if remove_me.next is None:
            self.tail = remove_me.prev
            if self.tail:
                self.tail.next = None
            else: # This is because the tail and the head are the same.
                self.tail = remove_me
            return
        if remove_me.prev is not None:
            remove_me.prev.next = remove_me.next
            remove_me.next = remove_me.prev
            return

    def _at_capacity(self) -> bool:
        return self.size == self.capacity

    def _remove_oldest(self):
        del self.itemsD[self.tail.key]
        new_tail = self.tail.prev
        self.tail = new_tail
        self.tail.next = None

    # Only use for debugging purposes
    def __str__(self) -> str:
        s = f"Head({self.head.value})\n"
        s += f"Tail({self.tail.value})"
        return s

# Test 1 given to us
print("\nSample Test provided to us")
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Test 2 - setting the same element a bunch to ensure we are not evicting good elements
print("\nStarting Test 2 - setting the same element a bunch to ensure we are not evicting good elements")
our_cache = LRU_Cache(5)
our_cache.set(2, 2)
our_cache.set(1, 1)
our_cache.set(1, 1)
our_cache.set(1, 1)
our_cache.set(1, 1)
our_cache.set(1, 1)
our_cache.get(1) # returns 1
print(our_cache.get(2)) 
# returns 2

# Test 3 - negative capacity
print("\nStarting Test 3 - setting a negative capacity in the cache")
our_cache = LRU_Cache(-1)
our_cache.set(3,3)
print(our_cache.get(3))
#returns 3
print(our_cache.get(2))
# returns -1
our_cache.set(2,2)
print(our_cache.get(3))
# returns -1
print(our_cache.get(2))
# returns 2

# Test 4 - setting a None type object in the cache
print("\nStarting Test 4 - setting a None type object in the cache")
our_cache = LRU_Cache(5)
our_cache.set(None, 5)
print(our_cache.get(None))
#returns -1