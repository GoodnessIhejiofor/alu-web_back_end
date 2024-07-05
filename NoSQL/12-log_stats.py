#!/usr/bin/env python3
"""log stats from collection
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection):
    """ script that provides some stats about Nginx logs stored in MongoDB
    """
    # Count total logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count logs by method
    print("Methods:")
    for method in METHODS:
        method_count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count status check
    status_check_count = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Print log stats
    log_stats(nginx_collection)
