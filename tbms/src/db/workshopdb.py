from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from db.networkdb import ConnectionString, Server
from db.resourcesdb import ReferenceMaterial, Survey

Base = declarative_base()


class VirtualMachine(Base):
    """
    Fields:
        id | name | file_location | vrdp | network_adapters(n:n) | host_server (n:1) | snapshots (1:n) |
        connection string (1:1)
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
    connection_string = relationship("ConnectionString", uselist=False, back_populates="virtual_machine")

    # References
    wu_id = Column(Integer, ForeignKey("workshop_unit.id"))


class WorkshopUnit(Base):
    """
    Fields:
        id | name | description | vms (1:n) | status | host server (n:1) | reference materials (n:n) |
        connection strings (1:n) | session lifetime | published date | surveys (n:n)
    """
    __tablename__ = "workshop_unit"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    status = Column(String)
    lifetime = Column(Integer)  # Amount of time the session is supposed to stay active
    published_date = Column(Date)

    # VMs have a 1:n relationship
    vms = relationship("VirtualMachine")

    # host server has a n:1 relationship
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship("Server")

    # connection strings have a 1:n relationship
    connection_strings = relationship("ConnectionString")

    # reference materials have a n:n relationship
    reference_materials = relationship("ReferenceMaterial", secondary=unit_references)

    # surveys have a n:n relationship
    surveys = relationship("Survey", secondary=unit_surveys)

    # References
    session_id = Column(Integer, ForeignKey('session.id'))
    session = relationship('Session', back_populates='workshop_unit')


class WorkshopGroup(Base):
    """
    Fields:
        id | name | description | WUs (1:n) | status | host server (n:1) | reference materials (n:n) |
        surveys (1:n) | published date | session lifetime
    """
    __tablename__ = "workshop_group"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    status = Column(String)
    lifetime = Column(Integer)  # Amount of time the session is supposed to stay active
    published_date = Column(Date)

    # VMs have a 1:n relationship
    wus = relationship("WorkshopUnit")

    # host server has a n:1 relationship
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship("Server")

    # reference materials have a n:n relationship
    reference_materials = relationship("ReferenceMaterial", secondary=group_references)

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


vm_adapters = Table('vm_adapters', Base.metadata,
                    Column('vm_id', Integer, ForeignKey('virtual_machine.id')),
                    Column('network_id', Integer, ForeignKey('network_adapter.id'))
                    )

unit_references = Table('unit_references', Base.metadata,
                        Column('unit_id', Integer, ForeignKey('workshop_unit.id')),
                        Column('reference_id', Integer, ForeignKey('reference_material.id'))
                        )

unit_surveys = Table('unit_surveys', Base.metadata,
                     Column('unit_id', Integer, ForeignKey('workshop_unit.id')),
                     Column('survey_id', Integer, ForeignKey('survey.id'))
                     )

group_references = Table('group_references', Base.metadata,
                         Column('group_id', Integer, ForeignKey('workshop_group.id')),
                         Column('reference_id', Integer, ForeignKey('reference_material.id'))
                         )

group_surveys = Table('group_surveys', Base.metadata,
                      Column('group_id', Integer, ForeignKey('workshop_group.id')),
                      Column('survey_id', Integer, ForeignKey('survey.id'))
                      )
