#!/usr/bin/env python3
"""
LRU caching
"""
BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    """
    LRU Caching implimentation 
    """
    def __init__(self):
        """
        Initializer for the class LRU
        """
        super().__init__()
    
    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first = sorted(self.cache_data.keys())[0]
            print(f"DISCARD: {first}")
            self.cache_data.pop(first)
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None and key not in self.cache_data:
            return
        item = self.cache_data.pop(key, None)
        self.cache_data[key] = item
        return item