from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.db_def import NetworkAdapter

import hashlib

engine = create_engine('sqlite:///test.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

adapter = NetworkAdapter(name="nw_ad1")

session.add(adapter)
session.commit()
