import datetime

from db_manager import WorkshopDB as workshop
from db_manager import UserDB as user
from db_manager import NetworkDB as network

"""vm1 = {
    'name': 'vm1',
    'file_name': 'c://vm/goes/here/vm1',
    'vrdp': 333,
    'server_id': 1,
    'wu_id': 1
}

vm2 = {
    'name': 'vm2',
    'file_name': 'c://vm/goes/here/vm2',
    'vrdp': 334,
    'server_id': 1,
    'wu_id': 1
}

vm3 = {
    'name': 'vm3',
    'file_name': 'c://vm/goes/here/vm3',
    'vrdp': 335,
    'server_id': 1,
    'wu_id': 2
}

vm4 = {
    'name': 'vm4',
    'file_name': 'c://vm/goes/here/vm4',
    'vrdp': 336,
    'server_id': 1,
    'wu_id': 2
}"""

wu1 = {
    'name': 'wu1',
    'description': 'Pls lord baby jesus work',
    'session': 'N/A',
    'status': 'N/A',
    'lifetime': 9999,
    'published_date': datetime.date(2017, 8, 29),
    'server_id': 1,
    'wg_id': 1
}

wu2 = {
    'name': 'wu2',
    'description': 'Bob bless our soul',
    'session': 'N/A',
    'status': 'N/A',
    'lifetime': 9999,
    'published_date': datetime.date(2017, 11, 2),
    'server_id': 1,
    'wg_id': 1
}

wu3 = {
    'name': 'wu3',
    'description': 'Bob bless our soul yea',
    'session': 'N/A',
    'status': 'N/A',
    'lifetime': 9999,
    'published_date': datetime.date(2017, 11, 2),
    'server_id': 2,
    'wg_id': 1
}

wu4s = {
    'name': 'wu4s',
    'description': 'Standalone unit',
    'session': 'N/A',
    'status': 'N/A',
    'lifetime': 9999,
    'published_date': datetime.date(2017, 11, 2),
    'server_id': 2,
    'wg_id': -1
}

wu5s = {
    'name': 'wu5s',
    'description': 'Standalone unit',
    'session': 'N/A',
    'status': 'N/A',
    'lifetime': 9999,
    'published_date': datetime.date(2017, 11, 2),
    'server_id': 1,
    'wg_id': -1
}

wg1 = {
    'name': 'wg1',
    'description': 'It a group',
    'status': 'N/A',
    'lifetime': 111111,
    'published_date': datetime.date(2017, 1, 1),
    'server_id': 1
}

wg2 = {
    'name': 'wg2',
    'description': 'It a group again',
    'status': 'N/A',
    'lifetime': 111111,
    'published_date': datetime.date(2017, 1, 1),
    'server_id': 2
}



cred = {
    'username': 'admin',
    'password': 'e9e8707c6343bafe43891613343c56a4e5e4b06b2c473d7c6e765a037cd4e0c0',
    'salt': '67b176705b46206614219f47a05aee7ae6a3edbe850bbbe214c536b989aea4d2',
    'user_id': 1
}

cred2 = {
    'username': 'tkings',
    'password': '9345cf5510e1a72292afd24798ebdb67d0118df638dc05bea0d84dd83fb2ed61',
    'salt': 'b1b1bd1ed240b1496c81ccf19ceccf2af6fd24fac10ae42023628abbe2687310',
    'user_id': 2
}

user1 = {
    'first_name': 'Admin',
    'last_name': 'Nistrator',
    'organization': 'UTEP',
    'email': 'admin@tbms.edu',
    'skill_level': 'expert',
    'permissions': 1
}

user2 = {
    'first_name': 'Tech',
    'last_name': 'Kings',
    'organization': 'UTEP',
    'email': 'tkings@miners.utep.edu',
    'skill_level': 'beginner',
    'permissions': 2
}

server1 = {
    'ip': '192.168.0.17',
    'status': 'N/A',
    'username': 'Emmanuel',
    'password': 'Utep@124#012'
}

server2 = {
    'ip': '192.168.0.18',
    'status': 'N/A',
    'username': 'Vbox',
    'password': 'password'
}

"""workshop.create("virtual machine", vm1)
workshop.create("virtual machine", vm2)
workshop.create("virtual machine", vm3)
workshop.create("virtual machine", vm4)"""
workshop.create("workshop unit", wu1)
workshop.create("workshop unit", wu2)
workshop.create("workshop unit", wu3)
workshop.create("workshop unit", wu4s)
workshop.create("workshop unit", wu5s)
workshop.create("workshop group", wg1)
workshop.create("workshop group", wg2)

user.create("credentials", cred)
user.create("credentials", cred2)
user.create("user", user1)
user.create("user", user2)

network.create("server", server1)
network.create("server", server2)

vms = workshop.read("all vms")
wus = workshop.read("all wus")
wgs = workshop.read("all wgs")

cred = user.read("credentials", "admin")
users = user.read("all users")

servers = network.read("all servers")

for vm in vms:
    print(vm.name)

for wu in wus:
    print(wu.name)

for wg in wgs:
    print(wg.name)

for c in cred:
    print(c.user_id)

for u in users:
    print(u.id)

for s in servers:
    print(s.ip)
