#!/usr/bin/env python3
""" FIFO cache """

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache class """
    def __init__(self):
        """ Override superclass __init__ """
        super().__init__()
        self.queue = []
    
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.queue.pop(0)
                del self.cache_data[removed]
                print("DISCARD:", removed)
            self.queue.append(key)
            self.cache_data[key] = item
            
    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
