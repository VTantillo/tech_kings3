from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///demo.db', echo=True)
Session = sessionmaker(bind=engine)
