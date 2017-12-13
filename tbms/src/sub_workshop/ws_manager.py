"""
Interface for the workshop subsystem.
"""
import network_adapter
import snapshot
from workshop_unit import WorkshopUnit
from workshop_group import WorkshopGroup
from virtual_machine import VirtualMachine
from ..db.db_manager import WorkshopDB
import workshop_unit
import workshop_group


def create(item_name, fields):
    if item_name == 'virtual machine':
        # Add to Database
        """if WorkshopDB.update('virtual machine', fields):
            # vm in database so update
            pass
        else:
            WorkshopDB.create('virtual machine', fields)"""

        return VirtualMachine(fields['name'],
                              fields['id'],
                              fields['adapter'],
                              fields['port'],
                              fields['recent_snapshot'],
                              fields['host_ip'])


def read(item_name, item=None):
    return WorkshopDB.read(item_name, item)


def update():
    pass


def delete():
    pass


def clone():
    pass


def port():
    pass


def convert_query_list_to_wg_instance_list(wg_query_list):
    groups = []
    for g in wg_query_list:
        groups.append(WorkshopGroup(g.id, g.name, g.description, g.status, g.lifetime, g.published_date,
                                  g.server_id))
    return groups


def convert_query_list_to_wu_instance_list(wu_query_list):
    units = []
    for u in wu_query_list:
        units.append(WorkshopUnit(u.id, u.name, u.description, 'N/A', u.status, u.lifetime, u.published_date,
                                  u.server_id, u.wg_id))
    return units
