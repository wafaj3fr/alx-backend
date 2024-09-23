#!/usr/bin/env python3
""" LFU cache """

from collections import OrderedDict
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache class """
    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = {}

    def put(self, key, item):
        """Assigns the item value for the key key."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.keys_freq[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                min_freq = min(self.keys_freq.values())
                lfu_keys = [k for k, v in self.keys_freq.items() if v == min_freq]
                if len(lfu_keys) > 1:
                    # Use LRU algorithm to discard the least recently used key
                    lfu_key = next(k for k in self.cache_data if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                del self.keys_freq[lfu_key]
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.keys_freq[key] = 1

    def get(self, key):
        """Returns the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data:
            return None
        self.keys_freq[key] += 1
        return self.cache_data[key]
