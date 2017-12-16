import datetime

from db_def import VirtualMachine
from db_def import WorkshopUnit
from db_def import WorkshopGroup
from db_def import Snapshot
from db_def import NetworkAdapter

from src.sub_db import Session

session = Session()


def add_vm(values):
    new_vm = VirtualMachine(name=values['name'],
                            file_name=values['file_name'],
                            vrdp=values['vrdp'],
                            server_id=values['server_id'],
                            wu_id=values['wu_id'])
    session.add(new_vm)
    session.commit()


def add_wu(values):
    new_wu = WorkshopUnit(name=values['name'],
                          description=values['description'],
                          status=values['status'],
                          lifetime=values['lifetime'],
                          published_date=values['published_date'],
                          server_id=values['server_id'],
                          wg_id=values['wg_id'])

    session.add(new_wu)
    session.commit()


def add_wg(values):
    new_wg = WorkshopGroup(name=values['name'],
                           description=values['description'],
                           status=values['status'],
                           lifetime=values['lifetime'],
                           published_date=values['published_date'],
                           server_id=values['server_id'])
    session.add(new_wg)
    session.commit()


def add_snapshot(values):
    new_snap = Snapshot(date=values['date'], file_name=values['file_name'])
    session.add(new_snap)
    session.commit()


def add_network_adapter(values):
    new_net = NetworkAdapter(name=values['name'])
    session.add(new_net)
    session.commit()


def get_vm(vm_id):
    res = session.query(VirtualMachine).filter(VirtualMachine.id == vm_id)
    return res


def get_wu(wu_id):
    res = session.query(WorkshopUnit).filter(WorkshopUnit.id == wu_id)
    return res


def get_wg(wg_id):
    res = session.query(WorkshopGroup).filter(WorkshopGroup.id == wg_id)
    return res


def get_snapshot(snap_id):
    res = session.query(Snapshot).filter(Snapshot.id == snap_id)
    return res


def get_network_adapter(net_id):
    res = session.query(NetworkAdapter).filter(NetworkAdapter.id == net_id)
    return res


def get_all_vms():
    res = session.query(VirtualMachine).all()
    return res


def get_all_wus():
    res = session.query(WorkshopUnit).all()
    return res


def get_all_wgs():
    res = session.query(WorkshopGroup).all()
    return res


def get_server_wus(server_id):
    res = session.query(WorkshopUnit).filter(
        WorkshopUnit.server_id == server_id).filter(
        WorkshopUnit.wg_id != -1).all()
    return res


def get_server_wgs(server_id):
    res = session.query(WorkshopGroup).filter(
        WorkshopGroup.server_id == server_id).all()
    return res


def get_server_standalone(server_id):
    res = session.query(WorkshopUnit).filter(
        WorkshopUnit.server_id == server_id).filter(
        WorkshopUnit.wg_id == -1).all()
    return res


def update_vm(vm_id, values):
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


def update_wu(wu_id, values):
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


def update_wg(wg_id, values):
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


def update_snapshot(snap_id, values):
    snap = get_snapshot(snap_id)
    if 'name' in values:
        snap.name = values['name']
    if 'file_name' in values:
        snap.file_name = values['file_name']


def update_network_adapter(net_id, values):
    net = get_network_adapter(net_id)
    if 'name' in values:
        net.name = values['name']

    session.commit()


def delete_vm(vm_id):
    vm = get_vm(vm_id)
    session.delete(vm)
    session.commit()


def delete_wu(wu_id):
    wu = get_wu(wu_id)
    session.delete(wu)
    session.commit()


def delete_wg(wg_id):
    wg = get_vm(wg_id)
    session.delete(wg)
    session.commit()


def delete_snapshot(snap_id):
    snap = get_snapshot(snap_id)
    session.delete(snap)
    session.commit()


def delete_network_adapter(na_id):
    na = get_vm(na_id)
    session.delete(na)
    session.commit()


def delete_all_vms():
    vms = get_all_vms()
    session.delete(vms)
    session.commit()


def delete_all_wus():
    wus = get_all_wus()
    session.delete(wus)
    session.commit()


def delete_all_wgs():
    wgs = get_all_wgs()
    session.delete(wgs)
    session.commit()
