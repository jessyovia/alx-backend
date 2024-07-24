#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.order.pop()
                print(f"DISCARD: {discarded}")
                self.cache_data.pop(discarded)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
