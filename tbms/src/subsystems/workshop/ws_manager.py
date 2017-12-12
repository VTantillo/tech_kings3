"""
Interface for the workshop subsystem.
"""
import network_adapter
import snapshot
from virtual_machine import VirtualMachine
from ..db.db_manger import WorkshopDB
import workshop_unit
import workshop_group


def create(item_name, fields):
    if item_name == 'vm':
        if WorkshopDB.update('vm', fields['id'], fields):
            # vm in database so update
            pass
        else:
            WorkshopDB.add('vm', fields['id'], fields)
        return VirtualMachine(fields['name'],
                              fields['id'],
                              fields['adapter'],
                              fields['port'],
                              fields['recent_snapshot'],
                              fields['host_ip'])


def read():
    pass


def update():
    pass


def delete():
    pass


def clone():
    pass


def port():
    pass
