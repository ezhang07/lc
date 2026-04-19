class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    # remove a certain node from doubly linked list
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    # insert to right most
    def insert(self, node):
        temp = self.right.prev
        temp.next = node
        node.prev = temp
        self.right.prev = node
        node.next = self.right
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
            
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            if len(self.cache) == self.capacity:
                lru = self.left.next
                self.remove(lru)
                self.cache.pop(lru.key)
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])




"""
key exists: update value of key

key doesn't exist:
    empty spot in dict: add key-value pair to cache
    full dict: remove LRU key, then add new key-value pair
"""