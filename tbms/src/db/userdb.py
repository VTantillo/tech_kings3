from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class User(Base):
    """
    Information about REGISTERED users
    Fields:
        id | first name | last name | organization | email | skill level | credentials (1:1)
        workshop history    // might need another table for dis
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    organization = Column(String)
    email = Column(String)
    skill_level = Column(String)
    credentials = relationship("Credentials", uselist=False, back_populates="user")

    # References
    session_id = Column(Integer, ForeignKey('session.id'))
    session = relationship('Session', back_populates='user')


class Credentials(Base):
    """
    Fields:
        user id | username | password
    """
    __tablename__ = "credentials"

    username = Column(String)
    password = Column(String)

    # References
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='credentials')



class Permissions(Base):
    """
    Specifies what the user can do in the systems
    """

    #todo: Figure out how we are going to deal with the permissions
