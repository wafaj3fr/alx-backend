#!/usr/bin/env python3
""" Basic dictionary """

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache class """
    def __init__(self):
        """ Override superclass __init__ """
        super().__init__()
        self.usage = []
        
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.usage.pop(0)
                del self.cache_data[removed]
                print("DISCARD:", removed)
            if key in self.usage:
                self.usage.remove(key)
            self.usage.append(key)
            self.cache_data[key] = item
            
    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache_data[key]
        return None
