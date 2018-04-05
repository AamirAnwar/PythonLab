class HashEntry(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None


class HashTable(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cur_capacity = 0
        self.slots = [None]*capacity

    def get(self, key):
        key_hash = hash(key)
        slot = key_hash % self.capacity

        t = self.slots[slot]

        while t != None and t.key != key:
            t = t.next
        return t

    def set(self, key, value):
        key_hash = hash(key)
        slot = key_hash % self.capacity

        if self.slots[slot] == None:
            self.slots[slot] = HashEntry(key,value)
        else:
            t = self.slots[slot]
            while t.next != None:
                t = t.next
            t.next = HashEntry(key,value)
        self.cur_capacity += 1