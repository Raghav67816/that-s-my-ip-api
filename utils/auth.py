"""
auth.py
Serves authentication related functions to the API.
"""
# Import dependencies
from secrets import token_hex
from utils.db import UserDataQuery
from passlib.context import CryptContext
from ipaddress import ip_address, IPv4Address, IPv6Address

user_db_query = UserDataQuery()
pwd_context = CryptContext(schemes=["bcrypt"])

# Create password hash - Converts plain password to hashed password.
def create_password_hash(plain_password: str):
    return pwd_context.hash(plain_password)

# Verify password hash - Verifies plain password with hashed password
def verify_password_hash(plain_password: str, password_hash: str):
    return pwd_context.verify(plain_password, password_hash)

# Validate user - Check if user already exists
def check_user(username: str, email: str):
    user_email = user_db_query.get_user_data(username, "Email")
    if user_email is None: # User does not exist and user can signup with these credentials.
        return 1

    elif user_email is not None and user_email == email:  # User records found with given email.
        return 0

# Authenticate user
def authenticate_user(name: str, password: str):
    user_data = user_db_query.get_user_data(name, "Name")
    if user_data is None:
        return 0

    elif user_data is not None:
        user_password = user_db_query.get_user_data(name, "Password")
        password_verify = verify_password_hash(password, user_password)
        if password_verify:
            return 1

        elif not password_verify:
            return 0

# Validate request - Check if request is sent with name and api key
def validate_request(name: str, api_key: str):
    user_data = user_db_query.get_user_data(name, "Name")
    if user_data is None:
        return 3

    elif user_data is not None:
        key = user_db_query.get_user_data(name, "API Key")
        if api_key == key:
            return 1

        elif api_key != key:
            return 0

# Generate API key
def generate_api_key():
    key = token_hex(16)
    return str(key)

# Check if ip address is valid
def check_ip(target_ip: str):
    try:
        ip_val = ip_address(target_ip)
        return 1

    except ValueError:
        return 0
