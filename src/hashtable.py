# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # # part 2
        # # Sets the index by using the hash method on the entered key
        index = self._hash_mod(key)
        # # Makes a key value pair off of input key and value
        pair = self.storage[index]
        # If a key exists in that index
        if self.storage[index] != None:
            pair = self.storage[index]
            # While "current pair" exists
            while pair:
                if pair.key == key:  # replace the value if key already exist
                    pair.value = value
                    print("warning override orccurd")
                    break
                elif pair.next:  # check next node
                    # The next node is set to that index
                    pair = pair.next
                else:
                    pair.next = LinkedPair(key, value)
                    break
        # Else if there is no other key that exists in that index
        else:
            # Set that index in storage to equal that pair
            self.storage[index] = LinkedPair(key, value)

        # # part 2
        # # Sets the index by using the hash method on the entered key
        # index = self._hash_mod(key)
        # # Makes a key value pair off of input key and value
        # pair = self.storage[index]
        # # If a key exists in that index add warning
        # if pair is not None:
        #     print("warning data will be overwritten")
        #     pair.key = key
        #     pair.value = value
        # # otherwise Set that index in storage to equal that pair
        # else:
        #     self.storage[index] = LinkedPair(key, value)

        # part 1
        # index = self._hash_mod(key)
        # lp = LinkedPair(key, value)

        # lp.next = self.storage[index]
        # self.storage[index] = lp

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # part 2
        # Sets the index by using the hash method on the entered key
        index = self._hash_mod(key)
        # # Makes a key value pair off of input key and value
        pair = self.storage[index]
        # here we check if our spot is not empty, and also if the key doesn't match the key in our node in that spot
        last = None
        # While "current pair" exists
        while (pair != None and pair.key != key):
            # if it doesn't, means we need to iterate over our LL until we find it, so we assign a temp var copy of our node
            last = pair
            # and we assign the current node to be the next node
            pair = pair.next
        # That index in storage equals None
        # if node is not, it means we did not found the node we want to delete, and we return None
        if (self.storage[index] == None):
            print("key not found!")
        else:
            if (last != None):
                # we assign the new head to be the next node
                last.next = pair.next
            else:
                # That item in storage
                self.storage[index] = pair.next

        # # part 2
        # # Sets the index by using the hash method on the entered key
        # index = self._hash_mod(key)
        # # If it is part of a linked list, loop through the pairs, until you find the matching "key"
        # if self.storage[index] is not None and self.storage[index].key == key:
        #     return self.storage[index].value
        # # Else print error
        # else:
        #     print("key not found!")
        # part 1
        # index = self._hash_mod(key)
        # lp = self.storage[index]
        # if lp:
        #     prev = None

        #     while True:
        #         if lp.key == key:
        #             if prev:
        #                 prev.next = lp.next
        #                 lp = None
        #                 break
        #             elif self.storage[index].next:
        #                 self.storage[index] = None
        #                 break
        #             else:
        #                 self.storage[index] = None
        #                 break
        #         else:
        #             if lp.next == None:
        #                 break
        # else:
        #     print("key not found!")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        lp = self.storage[index]

        if lp:
            while True:
                # and we check if there is no Node, and if the key
                if lp.key == key:
                    return lp.value
                else:
                    # if it does not match, we iterate
                    if lp.next:
                        lp = lp.next
                    else:
                        return None
                        # if node ends up being none, there is no node so we return none
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # increase capacity times 2
        self.capacity *= 2
        # we make a new storage with new capacity
        new_storage = [None] * self.capacity
        # set's old storage to capacity before increasing it
        old_storage = self.storage
        # we set our new storage to be our storage
        self.storage = new_storage
        # we iterate over the old storage
        for i in old_storage:
            if i:
                # we assign each value in current index to the new storage
                self.insert(i.key, i.value)
                lp = i
                while lp.next:
                    lp = lp.next
                    self.insert(lp.key, lp.value)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
