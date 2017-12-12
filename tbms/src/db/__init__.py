from . db_manger import WorkshopDB
from . db_manger import UserDB
from . db_manger import NetworkDB
from . db_manger import ResourceDB

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
