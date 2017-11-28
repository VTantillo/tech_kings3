from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from db.workshopdb import VirtualMachine

Base = declarative_base()


class Server(Base):
    """
    Columns:
        id
        ip
        status
        credentials
        ?? The units and groups that are on the server (probably could be done with queries)
    """
    __tablename__ = "server"

    id = Column(Integer, primary_key=True)


class Session(Base):
    """
    Columns:
        id
        user
        unit
        lifetime
        start time
    """
    __tablename__ = "session"


class ConnectionString(Base):
    """
    id
    file location
    """
    __tablename__ = "connection_string"

    id = Column(Integer, primary_key=True)
    file_location = Column(String)

    # References
    vm_id = Column(Integer, ForeignKey('virtual_machine.id'))
    vm = relationship("VirtualMachine", back_populates="connection_string")

    wu_id = Column(Integer, ForeignKey('workshop_unit.id'))


class Statistics(Base):
    """
    Columns:
        time stamp
        server
        no. of available connections
        no. of unused connections
        no. of used connections
        cpu usage
        memory usage
    """
    __tablename__ = "statistics"
