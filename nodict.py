#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Mike Boring'

from functools import total_ordering


class Node:
    def __init__(self, key, value=None):
        """define instance variables"""
        self.hash = hash(key)
        self.key = key
        self.value = value
        return

    def __repr__(self):
        """Return a string representing the Node contents."""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """Allow for comparison of nodes by key."""
        return self.key == other.key


class NoDict:
    def __init__(self, num_buckets=10):
        """define instance variables"""
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """Add a Node to Nodict"""
        new_node = Node(key, value)
        bucket_index = new_node.hash % self.size
        if len(self.buckets[bucket_index]) > 0:
            for i, ind_node in enumerate(self.buckets[bucket_index]):
                if ind_node == new_node:
                    self.buckets[bucket_index].remove(
                        self.buckets[bucket_index][i])
                    self.buckets[bucket_index].append(new_node)
                else:
                    self.buckets[bucket_index].append(new_node)
        else:
            self.buckets[bucket_index].append(new_node)
        return

    def get(self, key):
        """Checks for specified key and returns value or raises KeyError"""
        node_to_find = Node(key)
        bucket_index = node_to_find.hash % self.size
        for ind_node in self.buckets[bucket_index]:
            if ind_node.key == node_to_find.key:
                return ind_node.value
            else:
                continue
        raise KeyError(f'{key} not found')

    def __setitem__(self, key, value):
        """Enables square-bracket assignment behavior"""
        new_node = Node(key, value)
        bucket_index = new_node.hash % self.size
        if len(self.buckets[bucket_index]) > 0:
            for i, ind_node in enumerate(self.buckets[bucket_index]):
                if ind_node.key == new_node.key:
                    self.buckets[bucket_index].remove(
                        self.buckets[bucket_index][i])
                    self.buckets[bucket_index].append(new_node)
                else:
                    self.buckets[bucket_index].append(new_node)
        else:
            self.buckets[bucket_index].append(new_node)
        return

    def __getitem__(self, key):
        """Returns value from specified key"""
        node_to_find = Node(key)
        bucket_index = node_to_find.hash % self.size
        for ind_node in self.buckets[bucket_index]:
            if ind_node.key == node_to_find.key:
                return ind_node.value
            else:
                raise KeyError(f'{key} not found')
