import sqlite3

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# todo: STILL have no idea what to do about the polling durations for stuff
# todo: workshop history table??
# todo: server credentials table??
# todo: permissions
