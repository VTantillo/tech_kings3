from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from db.workshopdb import VirtualMachine, WorkshopUnit
from db.userdb import User

Base = declarative_base()


# todo: polling durations?
# todo: server credentials table
class Server(Base):
    """
    Fields:
        id | ip | status | credentials

        (Server credential table?)
    """
    __tablename__ = "server"

    id = Column(Integer, primary_key=True)
    ip = Column(String)
    username = Column(String)
    password = Column(String)


class Session(Base):
    """
    Fields:
        id | user (1:1) | unit (1:1) | lifetime | start time

        (Should it have an end time too?)
    """
    __tablename__ = "session"

    id = Column(Integer, primary_key=True)
    lifetime = Column(Integer)
    start_time = Column(Date)

    # user has a 1:1 relationship
    user = relationship("User", uselist=False, back_populates="session")

    # unit has a 1:1 relationship
    unit = relationship("WorkshopUnit", uselist=False, back_populates="session")


class ConnectionString(Base):
    """
    id | file name
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
        id | time stamp | server | no. of available connections |
        no. of unused connections | no. of used connections | cpu usage |
        memory usage
    """
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    time_stamp = Column(Date)
    available = Column(Integer)
    used = Column(Integer)
    unused = Column(Integer)
    cpu = Column(Integer)
    memory = Column(Integer)

    # server has n:1 relationship
    server_id = Column(Integer, ForeignKey("server.id"))
    server = relationship("Server")
