"""
Module containing a HashTable class implementation.

This module provides a basic hash table (hash map) implementation using separate chaining for collision handling.
The HashTable class supports operations like setting and getting items by key, retrieving all keys, and printing
the table contents.
"""


class HashTable:
    """
    A simple hash table implementation using separate chaining to handle collisions.

    Attributes:
        data_map (list): A list of buckets where each bucket holds key-value pairs.
    """

    def __init__(self, size=7):
        """
        Initializes the hash table with a fixed number of buckets.

        Args:
            size (int): The number of buckets in the hash table. Default is 7.
        """
        self.data_map = [None] * size

    def _hash(self, key):
        """
        Generates a hash value for the given key.

        Args:
            key (str): The key to hash.

        Returns:
            int: The index (hash value) of the key in the hash table.
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        """
        Adds a key-value pair to the hash table.

        If the bucket for the given key's hash index is empty, it creates a new list. Otherwise, it appends the
        key-value pair to the existing list.

        Args:
            key (str): The key for the item.
            value (any): The value associated with the key.
        """
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """
        Retrieves the value associated with the given key.

        Args:
            key (str): The key to search for.

        Returns:
            any: The value associated with the key, or None if the key is not found.
        """
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        """
        Retrieves all the keys in the hash table.

        Returns:
            list: A list of all keys stored in the hash table.
        """
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_table(self):
        """
        Prints the contents of the hash table, including each bucket and its key-value pairs.
        """
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
