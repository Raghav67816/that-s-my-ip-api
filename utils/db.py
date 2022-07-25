"""
db.py
This file contains functions that processes user queries to database.
"""

# Import dependencies
from dataclasses import dataclass
from pymongo.mongo_client import MongoClient
from IP2Location import IP2Location as ip_location

"""
Specify MongoDB connection URL. You must enter your's.
Remember: This creates a local connection to the database.
"""
connection_url = "mongodb://localhost:27017"
ip_database = ip_location("config/IP2LOCATION-LITE-DB11.IPV6.BIN")

# Configure db
def config_db(connection_url: str):
    client = MongoClient(connection_url)
    db = client["IP2Location"]  # Import IP2Location LITE DB11 CSV file.
    return db

# Setup connection to database
db = config_db(connection_url)

# User collection - MongoDB collection containing users data.
user_collection = db["Users"]

# User Data Query - Process user queries
class UserDataQuery:
    
    # Get user data
    @staticmethod
    def get_user_data(name: str, query: str):
        user_data = user_collection.find_one({"Name": name})
        if user_data is None:  # No user data found
            return None

        elif user_data is not None:  # User data found, returns a dict
            return user_data[query]

    # Update user details - Name only
    @staticmethod
    def update_user_details(name: str, new_name: str):
        try:
            user_data = user_collection.update_one({"Name": name}, {"$set": {"Name": new_name}})
            return 1

        except Exception as update_error:
            return str(update_error)

# Query Ip Address
def query_ip_address(target_ip: str):
    ip_data = ip_database.get_all(target_ip)  # Define target IP Address
    try:
        ip_data_dict = {
        "ip address": target_ip,
        "country short": ip_data.country_short,
        "country_long": ip_data.country_long,
        "region": ip_data.region,
        "city": ip_data.city,
        "latitude": ip_data.latitude,
        "longitude": ip_data.longitude,
        "zipcode": ip_data.zipcode,
        "timezone": ip_data.timezone,
        }
        return ip_data_dict  # Return output as dictionary

    except Exception as lookup_error:  # Handle error
        return str(lookup_error)  # Return error as string
