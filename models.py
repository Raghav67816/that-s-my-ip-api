"""
models.py
Contains fields to be included in request by clients.
"""

# Import dependencies
from pydantic import BaseModel
from pydantic import EmailStr

# User Model - SignUp
class User(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@doe.com",
                "password": "password@123"
            }
        }

# User Login Model - Login
class UserLogin(BaseModel):
    name: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "password": "password@123"
            }
        }

# IP Lookup
class Ip_Lookup(BaseModel):
    domain_or_ip: str
    name: str
    api_key: str
