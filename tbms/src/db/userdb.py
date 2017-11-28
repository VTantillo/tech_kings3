from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class User(Base):
    """
    Information about REGISTERED users
    Columns:
        id
        first name
        last name
        organization
        email
        skill level
        credentials
        workshop history    // might need another table for dis
    """
    __tablename__ = "user"


class Credentials(Base):
    """
    Columns:
        user id (Foreign key from user table)
        username
        password
    """
    __tablename__ = "credentials"
