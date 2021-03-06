'''
Implement a hash table using an array
'''
class HashTable:

    def __init__(self):
        # Initialize with an array of size 1000
        # The size will depend on the number of expected entries
        self.table = [None] * 1000
        self.num_items = 0

    def get(self, key):
        index = hash(key) % len(self.table)
        node = self.table[index]
        if node is None:
            return None
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def put(self, key, value):
        index = hash(key) % len(self.table)
        newNode = LinkedListNode(key, value)
        if self.table[index] is None:
            self.table[index] = newNode
            self.num_items += 1
        else:
            node = self.table[index]
            while node is not None:
                # If key is already found, update value
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            node.next = newNode
            self.num_items += 1

class LinkedListNode:

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
