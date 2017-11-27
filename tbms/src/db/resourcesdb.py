from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from db.userdb import User

Base = declarative_base()


class ReferenceMaterial(Base):
    """
    Fields:
        id | name | file location | type
    """
    __tablename__ = "reference_material"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    file_location = Column(String)
    type = Column(String)


class Survey(Base):
    """
    Fields:
        id | name | file location | completed (boolean) | user (1:1)
    """
    __tablename__ = "survey"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    file_location = Column(String)
    completed = Column(Boolean)
    user = relationship("User", uselist=False, back_populate="survey")
