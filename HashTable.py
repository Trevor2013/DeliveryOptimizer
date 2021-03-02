# HashTable.py contains the HashMap class and the associated insert, delete, update, and lookup functions.

class HashMap:

    # Initializes the class
    # O(N) complexity
    def __init__(self, initial_capacity = 40):
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # Inserts a new item into the hash table.
    # O(1) complexity
    def insert(self, key, item):
        hashKey = int(key) % len(self.map)
        keyValue = [key, item]
        if self.map[hashKey] is None:
            self.map[hashKey] = list([keyValue])
            return True
        else:
            for pair in self.map[hashKey]:
                if pair[0] == key:
                    pair[1] = item
                    return True
            self.map[hashKey].append(keyValue)
            return True

    # Updates an item in the hash table
    # O(1) complexity
    def update(self, key, value):
        hashKey = int(key) % len(self.map)
        key_hash = self.map[hashKey]
        if key_hash is not None:
            for pair in self.map[hashKey]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('Error updating, key: ' + key)

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # O(1) complexity
    def lookup(self, key):
        hashKey = int(key) % len(self.map)
        if self.map[hashKey] is not None:
            for pair in self.map[hashKey]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Removes an item with matching key from the hash table.
    # O(1) complexity
    def remove(self, key):
        hashKey = int(key) % len(self.map)
        if self.map[hashKey] is None:
            return False
        for i in range(0, len(self.map[hashKey])):
            if self.map[hashKey][i][0] == key:
                self.map[hashKey].pop(i)
                return True

