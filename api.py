"""
api.py
Main API file, contains all endpoints.

Response is returned as JSON by default.
"""

# Import dependencies
from fastapi import FastAPI

# Security imports
from fastapi.middleware.cors import CORSMiddleware

# Utility imports
from models import User, UserLogin, Ip_Lookup
from utils.db import user_collection, UserDataQuery, IPTools
from utils.auth import (
    check_ip, check_user, create_password_hash, generate_api_key, 
    authenticate_user, validate_request
    )

# App
app = FastAPI()
user_db_query = UserDataQuery()
ip_tools = IPTools()

# Middleware setup - security
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE"],
    allow_credentials=True
)

# Create new user
@app.post("/user/new")
async def create_user(user_details: User):
    user_check = check_user(user_details.name, user_details.email)
    if user_check == 1:  # SignUp granted
        user_data = {
            "Name": user_details.name,
            "Email": user_details.email,
            "Password": create_password_hash(user_details.password),
            "API Key": generate_api_key(),
        }

        user_collection.insert_one(user_data)  # Insert data
        return {"Results": "New user successfully created."}

    elif user_check == 0:  # SignUp denied
        return {"Results": "Error creating new user.", "Error": "Email already in use."}

# Login user
@app.post("/user/login")
async def login_user(user_login: UserLogin):
    user_auth = authenticate_user(user_login.name, user_login.password)
    if user_auth == 0:
        return {"Results": "Login failed.", "Error": "Invalid name or password."}

    elif user_auth == 1:
        return {"Results": "Login successfull."}

# Update user profile - Name only
@app.post("/user/update_profile")
async def update_profile(name: str, new_name: str):
    profile_update = user_db_query.update_user_details(name, new_name)
    if profile_update == 1:
        return {"Results": "Name updated successfuly"}

    if profile_update == type(str):
        return {"Results": "Error updating name.", "Error": str(profile_update)}

# Ip lookup
@app.post("/ip_lookup")
def ip_look_up(ip_details: Ip_Lookup):
    validate_ip = check_ip(ip_details.domain_or_ip)
    if validate_ip == 1:  # IP Address is valid
        validate_req = validate_request(ip_details.name, ip_details.api_key)
        if validate_req == 1:
            ip_records = ip_tools.query_ip_address(ip_details.domain_or_ip)
            return ip_records

        elif ip_records == type(str):
            return {"Results": "IP lookup failed.", "Error": str(validate_req)}

        elif validate_ip == 0:
            return {"Results": "IP lookup failed.", "Error": "Invalid API key."}

        elif validate_ip == 3:
            return {"Results": "IP lookup failed.", "Error": "Unknwon error"}

    elif validate_ip == 0:
        return {"Results": "Ip lookup failed.", "Error": "Invalid IP address."}

# Domain lookup
@app.post("/domain_lookup")
def domain_blacklist_check(domain_details: Ip_Lookup):
    validate_req = validate_request(domain_details.name, domain_details.api_key)
    if validate_req == 1:
        domain_checkup_result = ip_tools.domain_lookup(domain_details.domain_or_ip)
        return domain_checkup_result

    elif validate_request == type(str):
        return {"Results": "Domain blacklist check failed.", "Error": str(validate_request)}
