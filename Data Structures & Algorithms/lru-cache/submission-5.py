class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key : pointer to node with corresponding value
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # delete node, from linked list, re add it to most recently used side of linked list
        self.delete(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update the value
            self.delete(self.cache[key])
            # update the linked list, delete the old node, insert new one
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.left.next
                self.delete(lru_node)
                del self.cache[lru_node.key]
                
                # remove the lru key from cache, and remove from linked list.
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
            # just insert new node.

    # need helpers for insertion of node and deletion of node maybue a swapping function

    def delete(self, node):
        # remove pointers of keyed node and on the keyed node.
        left_adj = node.prev
        right_adj = node.next
        left_adj.next = right_adj
        right_adj.prev = left_adj
        node.next = node.prev = None
    
    def insert(self, node):
        # we create a node and isnert at mot recently used linked list side
        prev_mru = self.right.prev
        self.right.prev = node
        prev_mru.next = node
        node.next = self.right
        node.prev = prev_mru

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        

        
