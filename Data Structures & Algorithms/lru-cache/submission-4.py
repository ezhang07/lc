class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        penultimate_node = self.right.prev
        penultimate_node.next = node
        self.right.prev = node
        node.prev = penultimate_node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove the value from linked list, and then re-insert but at the right side (mru) 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            if len(self.cache.keys()) == self.capacity:
                # evict LRU key
                evicted = self.left.next
                self.remove(evicted)
                del self.cache[evicted.key]

            # add the new key value pair
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
