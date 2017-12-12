import traceback
from functools import wraps
from multiprocessing import Process

import time

from flask import Flask, render_template, request

from subsystems.user import usr_manager
from subsystems.network import net_manager
from subsystems.workshop import ws_manager
from vboxapi import VirtualBoxManager
from errors import login_error, users_guest_temporary_workshops_error, users_registered_temporary_workshops_error, \
    admin_servers_error
from tbms.src.subsystems.vboxapi.clienttest import enumToString


class Controller:

    def __init__(self):
        self.user = None
        self.servers = None

    def get_user(self):
        return self.user

    def set_user(self, u):
        self.user = u

    def get_servers(self):
        return self.servers

    def set_servers(self, s):
        self.servers = s

    def clean(self):
        self.user = None
        self.servers = None


app = Flask(__name__)
controller = Controller()


# Access control decorators
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if controller.get_user() is None:
            errors = {'page_error': "You need to log in for that"}
            return login_error(errors)
        elif controller.get_user().get_permissions() == 2:
            errors = {'page_error': "Access denied"}
            return users_registered_temporary_workshops_error(errors, controller.get_user())
        elif controller.get_user().get_permissions() == 3:
            errors = {'page_error': "Access denied"}
            return users_guest_temporary_workshops_error(errors, controller.get_user())
        return f(*args, **kwargs)

    return decorated_function


def registered_user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if controller.get_user() is None:
            errors = {'page_error': "You need to log in for that"}
            return login_error(errors)
        elif controller.get_user().get_permissions() == 1:
            errors = {'page_error': "Access denied"}
            return admin_servers_error(errors, controller.get_user())
        elif controller.get_user().get_permissions() == 3:
            errors = {'page_error': "Access denied"}
            return users_guest_temporary_workshops_error(errors, controller.get_user())
        return f(*args, **kwargs)

    return decorated_function


def guest_user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if controller.get_user() is None:
            errors = {'page_error': "You need to log in for that"}
            return login_error(errors)
        elif controller.get_user().get_permissions() == 1:
            errors = {'page_error': "Access denied"}
            return admin_servers_error(errors, controller.get_user())
        elif controller.get_user().get_permissions() == 2:
            errors = {'page_error': "Access denied"}
            return users_registered_temporary_workshops_error(errors, controller.get_user())
        return f(*args, **kwargs)

    return decorated_function


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/request/<logout>', methods=['POST', 'GET'])
def logout(logout):
    if logout == 'logout':
        print("Logout called " + logout)
        controller.clean()
        return login()
    else:
        print("Something else called this idk why")


@app.route('/', methods=['POST', 'GET'])
def login_auth():
    # Check if username or password is empty
    if request.form["username"] == "" or request.form["password"] == "":
        errors = {'login_error': "Empty username or password"}
        return login_error(errors)

    # usr_manager.authenticate return a User instance or None if user not in database
    controller.set_user(usr_manager.authenticate(request.form["username"], request.form["password"]))

    # Direct user to proper page or give error
    if controller.get_user() is None:
        errors = {'login_error': "Invalid username or password"}
        return login_error(errors)
    elif controller.get_user().get_permissions() == 1:

        # Get list of servers
        server_list = net_manager.read('servers')
        init_servers(server_list)
        # Get list of unit instances
        # Get list of workshop instances
        # Update servers in server list with wg, wu, wu(s), and vms that belong to that server

        print(server_list)
        # Add to controller
        controller.set_servers(server_list)
        return admin_servers()
    elif controller.get_user().get_permissions() == 2:
        return users_registered_temporary_workshops()
    elif controller.get_user().get_permissions() == 3:
        return users_guest_temporary_workshops()


@app.route('/administration/servers', methods=['POST', 'GET'])
@admin_required
def admin_servers():
    return render_template("administration/servers.html", user=controller.get_user(), servers=controller.get_servers())


@app.route('/administration/statistics', methods=['POST', 'GET'])
@admin_required
def admin_statistics():
    return render_template("administration/statistics.html", user=controller.get_user(),
                           servers=controller.get_servers())


@app.route('/administration/user_profiles', methods=['POST', 'GET'])
@admin_required
def admin_user_profiles():
    return render_template("administration/user_profiles.html", user=controller.get_user())


@app.route('/administration/virtual_machines', methods=['POST', 'GET'])
@admin_required
def admin_virtual_machines():
    return render_template("administration/virtual_machines.html", user=controller.get_user(),
                           servers=controller.get_servers())


@app.route('/administration/workshop_groups', methods=['POST', 'GET'])
@admin_required
def admin_workshop_groups():
    return render_template("administration/workshop_groups.html", user=controller.get_user(),
                           servers=controller.get_servers())


@app.route('/administration/workshop_units', methods=['POST', 'GET'])
@admin_required
def admin_workshop_units():
    return render_template("administration/workshop_units.html", user=controller.get_user(),
                           servers=controller.get_servers())


@app.route('/users/guest/temporary_workshops', methods=['POST', 'GET'])
@guest_user_required
def users_guest_temporary_workshops():
    return render_template("users/guest/temporary_workshops.html", user=controller.get_user())


@app.route('/users/registered/temporary_workshops', methods=['POST', 'GET'])
@registered_user_required
def users_registered_temporary_workshops():
    return render_template("users/registered/temporary_workshops.html", user=controller.get_user())


@app.route('/users/registered/persistence_workshops', methods=['POST', 'GET'])
@registered_user_required
def users_registered_persistence_workshops():
    return render_template("users/registered/persistence_workshops.html", user=controller.get_user())


def find_parent(snapshot):
    if snapshot != '':
        if snapshot.parent != "":
            return find_parent(snapshot.parent)
        else:
            return snapshot
    return snapshot


def get_most_recent(root, most_recent):
    if root.getChildrenCount() > 0:
        for child in root.children:
            most_recent = get_most_recent(child, most_recent)

    if root.timeStamp > most_recent.timeStamp:
        most_recent = root

    return most_recent


def init_servers(servers_list):
    print("Getting VM information from VirtualBox...")
    for server in servers_list:
        print("Getting VMs from " + server.get_ip() + "...")
        manager = VirtualBoxManager("WEBSERVICE", {
            'url': 'http://' + server.get_ip() + ':18083/',
            'user': server.get_username,
            'password': server.get_password})

        # Get the global VirtualBox object
        vbox = manager.getVirtualBox()


        # Make list of wg instances
        wg_list = []
        # Get list of wgs in this server from database (query all wg records that have this server as host)
        # Create list of wg instances
        # Add wg list for this server

        # Make list of wu instances
        wu_list = []
        # Get list of wus in this server from database (query all wu records that have this server as host)
        # Create list of wu instances
        # Add wu list for this server

        # Make list of vm instances
        vm_list = []
        # Get vms in this server from vbox and create list of vm instances
        # Enumerate all defined machines
        for machine in manager.getArray(vbox, 'machines'):
            print("Machine retrieved")
            vmname = str(machine.name)
            vmid = str(machine.id)
            vmadapter = str(machine.getNetworkAdapter(0).internalNetwork)
            vmVRDEserver = machine.VRDEServer
            vmport = str(vmVRDEserver.getVRDEProperty(u'TCP/Ports'))
            parent_snapshot = find_parent(machine.currentSnapshot)
            if parent_snapshot != '':
                most_recent = get_most_recent(parent_snapshot, parent_snapshot)
                recent_snapshot = str(most_recent.name)
            else:
                recent_snapshot = 'No snapshot'
            vm_fields = {'name': vmname,
                         'id': vmid,
                         'adapter': vmadapter,
                         'port': vmport,
                         'recent_snapshot': recent_snapshot,
                         'host_ip': server.get_ip()
                         }
            vm_instance = ws_manager.create('vm', vm_fields)
            vm_list.append(vm_instance)
            print("Machine added to vm list")

        # Add vm list for this server
        server.set_vms(vm_list)
        del manager

    return vm_list


def ping_loop():
    while True:
        print("Pinging 192.168.0.18..")
        manager = VirtualBoxManager("WEBSERVICE", {
            'url': 'http://192.168.0.18:18083/',
            'user': 'Vbox',
            'password': 'password'})

        # Get the global VirtualBox object
        vbox = manager.getVirtualBox()
        # Get all constants through the Python manager code
        vboxConstants = manager.constants
        # Enumerate all defined machines
        for machine in manager.getArray(vbox, 'machines'):
            try:
                # Be prepared for failures - the VM can be inaccessible
                vmname = '<inaccessible>'
                try:
                    vmname = machine.name
                except Exception as e:
                    None

                vmid = '';
                try:
                    vmid = machine.id
                except Exception as e:
                    None

                vmadapter = machine.getNetworkAdapter(0).internalNetwork
                print("Adapter Name: " + str(vmadapter))

                vmVRDEServer = machine.VRDEServer
                print("Port: " + str(vmVRDEServer.getVRDEProperty(u'TCP/Ports')))

                parent_snapshot = find_parent(machine.currentSnapshot)

                if parent_snapshot != '':
                    most_recent = get_most_recent(parent_snapshot, parent_snapshot)
                    print("Most recent Snapshot: " + str(most_recent.name))
                else:
                    print("No snapshot")

                # Print some basic VM information even if there were errors
                print("Machine name: %s [%s]" % (vmname, vmid))
                if vmname == '<inaccessible>' or vmid == '':
                    continue

                # Print some basic VM information
                print("    State:           %s" % (enumToString(vboxConstants, "MachineState", machine.state)))
                print("    Session state:   %s" % (
                    enumToString(vboxConstants, "SessionState", machine.sessionState)))

                # Do some stuff which requires a running VM
                if machine.state == vboxConstants.MachineState_Running:

                    # Get the session object
                    session = manager.getSessionObject()

                    # Lock the current machine (shared mode, since we won't modify the machine)
                    machine.lockMachine(session, vboxConstants.LockType_Shared)

                    # Acquire the VM's console and guest object
                    console = session.console
                    guest = console.guest

                    # Retrieve the current Guest Additions runlevel and print
                    # the installed Guest Additions version
                    addRunLevel = guest.additionsRunLevel
                    print("    Additions State: %s" % (
                        enumToString(vboxConstants, "AdditionsRunLevelType", addRunLevel)))
                    if addRunLevel != vboxConstants.AdditionsRunLevelType_None:
                        print("    Additions Ver:   %s" % (guest.additionsVersion))

                    # Get the VM's display object
                    display = console.display

                    # Get the VM's current display resolution + bit depth + position
                    screenNum = 0  # From first screen
                    (screenW, screenH, screenBPP, screenX, screenY, _) = display.getScreenResolution(screenNum)
                    print("    Display (%d):     %dx%d, %d BPP at %d,%d" % (
                        screenNum, screenW, screenH, screenBPP, screenX, screenY))

                    # We're done -- don't forget to unlock the machine!
                    session.unlockMachine()

            except Exception as e:
                print("Errror [%s]: %s" % (machine.name, str(e)))
                traceback.print_exc()
            print(
                "-----------------------------------------------------------------------------------------------------")
        # Call destructor and delete manager
        del manager
        seconds = 600
        while seconds >= 0:
            # print("Ping in "+str(seconds)+" seoonds...")
            time.sleep(1)
            seconds = seconds - 1


if __name__ == "__main__":
    # p = Process(target=ping_loop)
    # p.start()
    app.run()
    # p.join()
