"""
Describes the tables of the database in SQLAlchemy declarative language
"""

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from db import engine

Base = declarative_base()

# Workshop subsystem stuff
# n:n tables
vm_adapters = Table('vm_adapters', Base.metadata,
                    Column('vm_id', Integer,
                           ForeignKey('virtual_machine.id')),
                    Column('network_id', Integer,
                           ForeignKey('network_adapter.id'))
                    )

unit_references = Table('unit_references', Base.metadata,
                        Column('unit_id', Integer,
                               ForeignKey('workshop_unit.id')),
                        Column('reference_id', Integer,
                               ForeignKey('reference_material.id'))
                        )

unit_surveys = Table('unit_surveys', Base.metadata,
                     Column('unit_id', Integer,
                            ForeignKey('workshop_unit.id')),
                     Column('survey_id', Integer,
                            ForeignKey('survey.id'))
                     )

group_references = Table('group_references', Base.metadata,
                         Column('group_id', Integer,
                                ForeignKey('workshop_group.id')),
                         Column('reference_id', Integer,
                                ForeignKey('reference_material.id'))
                         )

group_surveys = Table('group_surveys', Base.metadata,
                      Column('group_id', Integer,
                             ForeignKey('workshop_group.id')),
                      Column('survey_id', Integer, ForeignKey('survey.id'))
                      )

user_history = Table('user_history', Base.metadata,
                     Column('user_id', Integer,
                            ForeignKey('user.id')),
                     Column('unit_id', Integer, ForeignKey('workshop_unit.id'))
                     )


class VirtualMachine(Base):
    """
    Fields:
        id | name | file_location | vrdp | network_adapters(n:n) |
        host_server (n:1) | snapshots (1:n) | connection string (1:1)
    """
    __tablename__ = "virtual_machine"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    file_name = Column(String)
    vrdp = Column(Integer)

    # network adapters have an n:n relationship
    network_adapters = relationship("NetworkAdapter", secondary=vm_adapters)

    # the host server has an n:1 relationship
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship("Server")

    # snapshots have an 1:n relationship
    snapshots = relationship("Snapshot")

    # connection strings have a 1:1 relationship
    connection_string = relationship("ConnectionString", uselist=False,
                                     back_populates="virtual_machine")

    # References
    wu_id = Column(Integer, ForeignKey("workshop_unit.id"))


class WorkshopUnit(Base):
    """
    Fields:
        id | name | description | vms (1:n) | status | host server (n:1) |
        reference materials (n:n) | connection strings (1:n) |
        session lifetime | published date | surveys (n:n)
    """
    __tablename__ = "workshop_unit"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    status = Column(String)
    # Length of time the session is to stay active
    lifetime = Column(Integer)
    published_date = Column(Date)

    # VMs have a 1:n relationship
    vms = relationship("VirtualMachine")

    # host server has a n:1 relationship
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship("Server")

    # connection strings have a 1:n relationship
    connection_strings = relationship("ConnectionString")

    # reference materials have a n:n relationship
    reference_materials = relationship("ReferenceMaterial",
                                       secondary=unit_references)

    # surveys have a n:n relationship
    surveys = relationship("Survey", secondary=unit_surveys)

    # References
    wg_id = Column(Integer, ForeignKey("workshop_group.id"))

    session_id = Column(Integer, ForeignKey('session.id'))
    session = relationship('Session', back_populates='workshop_unit')


class WorkshopGroup(Base):
    """
    Fields:
        id | name | description | WUs (1:n) | status | host server (n:1) |
        reference materials (n:n) | surveys (1:n) | published date |
        session lifetime
    """
    __tablename__ = "workshop_group"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    status = Column(String)
    # Amount of time the session is supposed to stay active
    lifetime = Column(Integer)
    published_date = Column(Date)

    # WUs have a 1:n relationship
    wus = relationship("WorkshopUnit")

    # host server has a n:1 relationship
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship("Server")

    # reference materials have a n:n relationship
    reference_materials = relationship("ReferenceMaterial",
                                       secondary=group_references)

    # surveys have a n:n relationship
    surveys = relationship("Survey", secondary=group_surveys)


class Snapshot(Base):
    """
    Fields:
        id | date | file name

        state?? (idk how snapshots work tbh)
    """
    __tablename__ = "snapshot"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    file_name = Column(String)

    # References
    vm_id = Column(Integer, ForeignKey('virtual_machine.id'))


class NetworkAdapter(Base):
    """
    Fields:
        id | name
    """
    __tablename__ = "network_adapter"

    id = Column(Integer, primary_key=True)
    name = Column(String)


# User subsystem stuff
class User(Base):
    """
    Information about REGISTERED users
    Fields:
        id | first name | last name | organization | email | skill level |
        credentials (1:1) | workshop history
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    organization = Column(String)
    email = Column(String)
    skill_level = Column(String)
    credentials = relationship("Credentials", uselist=False,
                               back_populates="user")
    permissions = Column(Integer, nullable=False)

    # unit has an n:n relationship
    workshop_history = relationship("WorkshopUnit", secondary='user_history')

    # References
    session_id = Column(Integer, ForeignKey('session.id'))
    session = relationship('Session', back_populates='user')


class Credentials(Base):
    """
    Fields:
        user id | username | password
    """
    __tablename__ = "credentials"

    username = Column(String, unique=True)
    password = Column(String)
    salt = Column(String)

    # References
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship('User', back_populates='credentials')


# Network subsystem stuff
class Server(Base):
    """
    Fields:
        id | ip | status | credentials

        (Server credential table?)
    """
    __tablename__ = "server"

    id = Column(Integer, primary_key=True)
    ip = Column(String)
    status = Column(String)
    username = Column(String)
    password = Column(String)



class ServerCredentials(Base):
    """
    Fields:
        user id | username | password
    """
    __tablename__ = "server_credentials"

    username = Column(String)
    password = Column(String)
    salt = Column(String)

    # References
    server_id = Column(Integer, ForeignKey('server.id'), primary_key=True)
    server = relationship('Server', back_populates='server_credentials')


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
    workshop_unit = relationship("WorkshopUnit", uselist=False,
                                 back_populates="session")


class ConnectionString(Base):
    """
    id | file name
    """
    __tablename__ = "connection_string"

    id = Column(Integer, primary_key=True)
    file_location = Column(String)

    # References
    vm_id = Column(Integer, ForeignKey('virtual_machine.id'))
    virtual_machine = relationship("VirtualMachine",
                                   back_populates="connection_string")

    # I don't think we should have this reference.  The unit can get
    # the connection strings through its vms
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


# Resource subsystem stuff
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

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")


# Create tables
Base.metadata.create_all(engine)
