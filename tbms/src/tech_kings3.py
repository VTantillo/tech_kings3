from functools import wraps
from flask import Flask, render_template, request
from subsystems.user import usr_manager
from errors import login_error, users_guest_temporary_workshops_error, users_registered_temporary_workshops_error, admin_servers_error


class Controller:

    def __init__(self):
        self.user = None

    def get_user(self):
        return self.user

    def set_user(self, u):
        self.user = u

    def clean(self):
        self.user = None

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


@app.route('/<logout>', methods=['POST', 'GET'])
def logout(logout):
    print("Logout called "+logout)
    controller.clean()
    return login()


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
        return admin_servers()
    elif controller.get_user().get_permissions() == 2:
        return users_registered_temporary_workshops()
    elif controller.get_user().get_permissions() == 3:
        return users_guest_temporary_workshops()


@app.route('/administration/servers', methods=['POST', 'GET'])
@admin_required
def admin_servers():
    return render_template("administration/servers.html", user=controller.get_user())


@app.route('/administration/statistics', methods=['POST', 'GET'])
@admin_required
def admin_statistics():
    return render_template("administration/statistics.html", user=controller.get_user())


@app.route('/administration/user_profiles', methods=['POST', 'GET'])
@admin_required
def admin_user_profiles():
    return render_template("administration/user_profiles.html", user=controller.get_user())


@app.route('/administration/virtual_machines', methods=['POST', 'GET'])
@admin_required
def admin_virtual_machines():
    return render_template("administration/virtual_machines.html", user=controller.get_user())


@app.route('/administration/workshop_groups', methods=['POST', 'GET'])
@admin_required
def admin_workshop_groups():
    return render_template("administration/workshop_groups.html", user=controller.get_user())


@app.route('/administration/workshop_units', methods=['POST', 'GET'])
@admin_required
def admin_workshop_units():
    return render_template("administration/workshop_units.html", user=controller.get_user())


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


if __name__ == "__main__":
    app.run()
