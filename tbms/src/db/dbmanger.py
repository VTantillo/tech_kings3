import sqlite3

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# TODO: May need to split them up into their own files
# TODO: STILL have no idea what to do about the polling durations for stuff
# TODO: Permissions table??
# TODO: network adapter table??
# TODO: workshop history table??
# TODO: server credentials table??

db = sqlite3.connect("test.db")
cursor = db.cursor()

engine = create_engine('sqlite://test.db', echo=True)
Base = declarative_base()


# Workshop subsystem stuff
class VirtualMachine(Base):
    """
    Columns:
        id
        name
        file location
        vrdp
        network adapter (s) // might need another table for those...
        host server ip
        snapshots // point to the snapshot table
        os?
        info?
    """
    __tablename__ = "virtual_machine"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    file = Column(String)
    vrdp = Column(Integer)
    network_adapter = Column(Integer, ForeignKey("network_adapter.id"))
    snapshots = Column(Integer, ForeignKey("snapshot.id"))
    host = Column(Integer, ForeignKey("server.id"))
    connection_string = (Integer, ForeignKey("connection_string.id"))


class WorkshopUnit(Base):
    """
    Columns:
        id
        name
        description
        vms
        status
        host server ip
        reference materials
        connection strings
        session lifetime
        published date
    """
    __tablename__ = "workshop_unit"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    vms = Column(Integer, ForeignKey("virtual_machine.id"))
    status = Column(String)
    host = Column(Integer, ForeignKey("server.id"))
    reference_materials = Column(Integer, ForeignKey("ref"))
    connection_strings = Column(Integer, ForeignKey("connection_string"))
    lifetime = Column(Integer)
    published_date = Column(Date)
    surveys = Column(Integer, ForeignKey("survey"))


class WorkshopGroup(Base):
    """
    Columns:
        id
        name
        description
        wus
        status
        no. of units
        host server ip
        reference materials
        session lifetime
        published date
    """
    __tablename__ = "workshop_group"

    id = Column(Integer, primary_key=True)


class Snapshot(Base):
    """
    Columns:
        id
        vm
        date
        state??
        (idk how snapshots work tbh)
    """
    __tablename__ = "snapshot"

    id = Column(Integer, primary_key=True)


# User subsystem stuff
class User(Base):
    """
    Information about REGISTERED users
    Columns:
        id
        first name
        last name
        org
        email
        skill level
        credentials         // points to the credentials table
        workshop history    // might need another table for dis
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)


class Credentials(Base):
    """
    Columns:
        user id (Foreign key from user table)
        username
        hashed password
    """
    __tablename__ = "credentials"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    # MAKE SURE DIS SHIT IS HASHED SOMEWHERE
    password = Column(String)


# Network subsystem stuff
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

    id = Column(Integer, primary_key=True)
    # should probably be references rather than just the ids or names
    user = Column(String)
    unit = Column(String)


class Server(Base):
    """
    Columns:
        id
        ip
        username    // should these be in another table like the one for users
        password
        status
        ?? The units and groups that are on the server
    """
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True)


class ConnectionString(Base):
    """
    id
    file location
    """
    __tablename__ = "connection_string"


class Statistics(Base):
    """
    Columns:
        server
        no. of available connections
        no. of unused connections
        no. of used connections
        cpu usage
        memory usage
    """
    __tablename__ = "statistics"


# Resource subsystem stuff
class ReferenceMaterial(Base):
    """
    Columns:
        id
        name
        file location
        type
    """
    __tablename__ = "reference_material"


class Survey(Base):
    """
    Columns:
        id
        name
        file location
        completed (boolean)
        // if we are going to
    """
    __tablename__ = "survey"


