#!/usr/bin/env python3
""" Basic dictionary """

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class """
    def __init__(self):
        """ Override superclass __init__ """
        super().__init__()
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
            
    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
