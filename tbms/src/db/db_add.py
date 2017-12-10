from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.db_def import User, Credentials, Permissions

import hashlib

engine = create_engine('sqlite:///test.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

salt = "tech.kings"

sha = hashlib.sha3_256(b"tech.kings").hexdigest()

hash_salt = sha

password1 = "kings"
password2 = "tech"

salt1 = "one"
salt2 = "two"

hash_salt1 = salt1 + password1 + hash_salt
hash_salt2 = salt2 + password2 + hash_salt

hash_salt1 = hashlib.sha3_256(hash_salt1.encode()).hexdigest()
hash_salt2 = hashlib.sha3_256(hash_salt2.encode()).hexdigest()

user1 = User(
    first_name="Tech",
    last_name="Kings",
    organization="UTEP",
    email="tech.kings@utep.edu",
    skill_level="Expert"
)

user2 = User(
    first_name="Kings",
    last_name="Tech",
    organization="UTEP",
    email="kings.tech@utep.edu",
    skill_level="Novice"
)

credential1 = Credentials(
    username="Tech.Kings",
    password=hash_salt1,
    salt=salt1
)

credential2 = Credentials(
    username="Kings.Tech",
    password=hash_salt2,
    salt=salt2
)

user1.credentials = credential1
user2.credentials = credential2
users = [user1, user2]

session.add_all([user1, user2])
session.commit()
