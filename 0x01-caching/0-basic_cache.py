#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching
    """

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
