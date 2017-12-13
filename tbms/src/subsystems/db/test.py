import datetime

from db_manager import WorkshopDB as workshop

vm1 = {
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
}

wu1 = {
    'name': 'wu1',
    'description': 'Pls lord baby jesus work',
    'status': 'Available af',
    'lifetime': 9999,
    'published_date': datetime.date(2017, 8, 29),
    'server_id': 1,
    'wg_id': 1
}

wu2 = {
    'name': 'wu1',
    'description': 'Bob bless our soul',
    'status': 'Rekt',
    'lifetime': 9999,
    'published_date': datetime.date(2017, 11, 2),
    'server_id': 1,
    'wg_id': 1
}

wg1 = {
    'name': 'wg1',
    'description': 'It a group',
    'status': 'works?',
    'lifetime': 111111,
    'published_date': datetime.date(2017, 1, 1),
    'server_id': 1,
}

workshop.create("virtual machine", vm1)
workshop.create("virtual machine", vm2)
workshop.create("virtual machine", vm3)
workshop.create("virtual machine", vm4)

workshop.create("workshop unit", wu1)
workshop.create("workshop unit", wu1)

workshop.create("workshop group", wg1)


vms = workshop.read("all vms")
for vm in vms:
    print(vm.name)