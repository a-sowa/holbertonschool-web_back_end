#!/usr/bin/env python3
"""
    Function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """Returns mongo_collection"""
    return mongo_collection.find()
