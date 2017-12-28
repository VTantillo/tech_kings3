"""
Workshop subsystem specific operations that the db_manager will call.
"""
from db_def import VirtualMachine
from db_def import WorkshopUnit
from db_def import WorkshopGroup
from db_def import Snapshot
from db_def import NetworkAdapter

from src.sub_db import Session

session = Session()


def create(item, values):
    """
    :param item:
    :param values:
    :return:
    """
    new_id = -1
    if item == "virtual machine":
        new_vm = VirtualMachine(name = values['name'],
                                file_name = values['file_name'],
                                vrdp = values['vrdp'],
                                server_id = values['server_id'],
                                wu_id = values['wu_id'])
        session.add(new_vm)
        session.commit()

    if item == "workshop unit":
        new_wu = WorkshopUnit(name = values['name'],
                              description = values['description'],
                              status = values['status'],
                              lifetime = values['lifetime'],
                              published_date = values['published_date'],
                              server_id = values['server_id'],
                              wg_id = values['wg_id'])

        session.add(new_wu)
        session.commit()

    if item == "workshop group":
        new_wg = WorkshopGroup(name = values['name'],
                               description = values['description'],
                               status = values['status'],
                               lifetime = values['lifetime'],
                               published_date = values['published_date'],
                               server_id = values['server_id'])
        session.add(new_wg)
        session.commit()

    if item == "snapshot":
        new_snap = Snapshot(date = values['date'],
                            file_name = values['file_name'])
        session.add(new_snap)
        session.commit()

    if item == "network adapter":
        new_net = NetworkAdapter(name = values['name'])
        session.add(new_net)
        session.commit()


def read(item, item_id = None):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "virtual machine":
        res = session.query(VirtualMachine).filter(VirtualMachine.id == vm_id)
        return res

    if item == "workshop unit":
        res = session.query(WorkshopUnit).filter(WorkshopUnit.id == wu_id)
        return res

    if item == "workshop group":
        res = session.query(WorkshopGroup).filter(WorkshopGroup.id == wg_id)
        return res

    if item == "snapshot":
        res = session.query(Snapshot).filter(Snapshot.id == snap_id)
        return res

    if item == "network adapter":
        res = session.query(NetworkAdapter).filter(NetworkAdapter.id == net_id)
        return res

    if item == "all vms":
        res = session.query(VirtualMachine).all()
        return res

    if item == "all wus":
        res = session.query(WorkshopUnit).all()
        return res

    if item == "all wgs":
        res = session.query(WorkshopGroup).all()
        return res

    if item == "server wus":
        res = session.query(WorkshopUnit).filter(
            WorkshopUnit.server_id == server_id).filter(
            WorkshopUnit.wg_id != -1).all()
        return res

    if item == "server standalone":
        res = session.query(WorkshopUnit).filter(
            WorkshopUnit.server_id == server_id).filter(
            WorkshopUnit.wg_id == -1).all()
        return res

    if item == "server wgs":
        res = session.query(WorkshopGroup).filter(
            WorkshopGroup.server_id == server_id).all()
        return res


def update(item, item_id, values):
    """

    :param item:
    :param item_id:
    :param values:
    :return:
    """
    if item == "virtual machine":
        vm = get_vm(vm_id)
        if 'name' in values:
            vm.name = values['name']
        if 'file_name' in values:
            vm.file_name = values['file_name']
        if 'vrdp' in values:
            vm.vrdp = values['vrdp']
        if 'server_id' in values:
            vm.server_id = values['server_id']
        if 'wu_id' in values:
            vm.wu_id = values['wu_id']

        session.commit()

    if item == "workshop unit":
        wu = get_wu(wu_id)
        if 'name' in values:
            wu.name = values['name']
        if 'description' in values:
            wu.description = values['description']
        if 'status' in values:
            wu.status = values['status']
        if 'lifetime' in values:
            wu.lifetime = values['lifetime']
        if 'published_date' in values:
            wu.published_date = values['published_date']
        if 'server_id' in values:
            wu.server_id = values['server_id']
        if 'wg_id' in values:
            wu.wg_id = values['wg_id']
        if 'session_id' in values:
            wu.session_id = values['session_id']

        session.commit()

    if item == "workshop group":
        wg = get_wg(wg_id)
        if 'name' in values:
            wg.name = values['name']
        if 'description' in values:
            wg.description = values['description']
        if 'status' in values:
            wg.status = values['status']
        if 'lifetime' in values:
            wg.lifetime = values['lifetime']
        if 'published_date' in values:
            wg.published_date = values['published_date']
        if 'server_id' in values:
            wg.server_id = values['server_id']

        session.commit()

    if item == "snapshot":
        snap = get_snapshot(snap_id)
        if 'name' in values:
            snap.name = values['name']
        if 'file_name' in values:
            snap.file_name = values['file_name']

    if item == "network adapter":
        net = get_network_adapter(net_id)
        if 'name' in values:
            net.name = values['name']

        session.commit()


def delete(item, item_id):
    """

    :param item:
    :param item_id:
    :return:
    """
    if item == "virtual machine":
        vm = get_vm(vm_id)
        session.delete(vm)
        session.commit()

    elif item == "workshop unit":
        wu = get_wu(wu_id)
        session.delete(wu)
        session.commit()

    elif item == "workshop group":
        wg = get_vm(wg_id)
        session.delete(wg)
        session.commit()

    elif item == "snapshot":
        snap = get_snapshot(snap_id)
        session.delete(snap)
        session.commit()

    elif item == "network adapter":
        na = get_vm(na_id)
        session.delete(na)
        session.commit()

    elif item == "all vms":
        vms = get_all_vms()
        session.delete(vms)
        session.commit()

    elif item == "all wus":
        wus = get_all_wus()
        session.delete(wus)
        session.commit()

    elif item == "all wgs":
        wgs = get_all_wgs()
        session.delete(wgs)
        session.commit()

    elif item == "all snapshots":
        pass

    elif item == "all network adapters":
        pass
