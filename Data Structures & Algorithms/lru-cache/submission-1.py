class Node:
    def __init__(self,key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #map key to node
        
        self.left, self.right = Node(0, 0), Node(0, 0) #left = LRU, right = MRU
        #connecting the dummy node first, cache still empty
        self.left.next = self.right
        self.right.prev = self.left

    #helper functions, to help remove and insert node
    #removing from cache, at any position
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    #inserting from right
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #removing
            self.insert(self.cache[key]) #reinsert, now it's the most recently used
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
