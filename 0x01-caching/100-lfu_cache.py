#!/usr/bin/env python3
""" LFUCache module
"""
from base_caching import BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                candidates = [k for k, v in self.frequency.items() if v == min_freq]
                if len(candidates) > 1:
                    discarded = candidates[0]
                else:
                    discarded = candidates[0]
                print(f"DISCARD: {discarded}")
                self.cache_data.pop(discarded)
                self.frequency.pop(discarded)
                self.order.remove(discarded)
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order.append(key)

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        return self.cache_data[key]
