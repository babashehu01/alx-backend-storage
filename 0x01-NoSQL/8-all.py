#!/usr/bin/env python3
"""Defines list_all(mongo_collection) function
"""

import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
    mongo_collection: The pymongo collection object.

    Returns:
    A list of documents.
    """
    documents = []
    for document in mongo_collection.find():
        documents.append(document)

    return document
