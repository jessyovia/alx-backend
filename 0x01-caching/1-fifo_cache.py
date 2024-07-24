#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict

class FIFOCache(BaseCaching):
    """ FIFOCache class inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key and item:
            if key in self.cache_data:
                self.order.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.order.popitem(last=False)
                print(f"DISCARD: {discarded[0]}")
                self.cache_data.pop(discarded[0])
            self.cache_data[key] = item
            self.order[key] = None

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.move_to_end(key)
        return self.cache_data[key]
