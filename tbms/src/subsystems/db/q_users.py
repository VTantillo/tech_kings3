from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_demo import User
from db_demo import Credentials

engine = create_engine('sqlite:///C:\\Users\\Emmanuel\\PycharmProjects\\tech_kings3\\tbms\\src\\subsystems\\db\\demo.db')
Session = sessionmaker(bind=engine)

session = Session()


def add_user(val):
    new_user = User(first_name=val['first_name'],
                    last_name=val['last_name'],
                    organization=val['organization'],
                    email=val['email'],
                    skill_level=val['skill_level'],
                    permissions=val['permissions'])
    session.add(new_user)
    session.commit()


def add_credentials(val):
    new_cred = Credentials(user_id=val['user_id'],
                           username=val['username'],
                           password=val['password'],
                           salt=val['salt'])
    session.add(new_cred)
    session.commit()


def get_user(usr_id):
    res = session.query(User).filter(User.id == usr_id)
    return res


def get_credentials(usr_id):
    res = session.query(Credentials).filter(Credentials.username == usr_id)
    return res


def get_all_users():
    res = session.query(User).all()
    return res


def update_user(usr_id, val):
    user = get_user(usr_id)
    if 'first_name' in val:
        user.first_name = val['first_name']
    if 'last_name' in val:
        user.last_name = val['']
    if 'organization' in val:
        user.organization = val['organization']
    if 'email' in val:
        user.email = val['email']
    if 'skill_level' in val:
        user.skill_level = val['skill_level']
    if 'permissions' in val:
        user.permissions = val['permissions']
    if 'session_id' in val:
        user.session_id = val['session_id']

    session.commit()


def update_credentials(usr_id, val):
    credentials = get_credentials(usr_id)
    if 'username' in val:
        credentials.username = val['username']
    if 'password' in val:
        credentials.password = val['password']

    session.commit()


def delete_user(usr_id):
    user = get_user(usr_id)
    delete_credentials(usr_id)
    session.delete(user)
    session.commit()


def delete_credentials(usr_id):
    credentials = get_credentials(usr_id)
    session.delete(credentials)
    session.commit()

