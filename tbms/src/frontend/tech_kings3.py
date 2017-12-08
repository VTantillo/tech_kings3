import hashlib
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, g
from tbms.src.user.user_subsystem import UserManager

app = Flask(__name__)

user = None


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/')
def login_error(message):
    return render_template("login.html", error=message)


@app.route('/', methods=['POST', 'GET'])
def login_auth():
    # Check if username or password is empty
    if request.form["username"] == "" or request.form["password"] == "":
        return login_error("Empty username or password")

    # UserManager.auth return a User instance or None if user not in database
    g.user = UserManager.auth(request.form["username"], request.form["password"])

    # Direct user to proper page or give error
    if g.user is None:
        return login_error("Invalid username or password")
    elif g.user.get_permissions() == 1:
        return admin_servers()
    elif g.user.get_permissions() == 2:
        return users_registered_temporary_workshops()


@app.route('/administration/servers', methods=['POST', 'GET'])
@login_required
def admin_servers():
    return render_template("administration/servers.html")


@app.route('/administration/statistics', methods=['POST', 'GET'])
@login_required
def admin_statistics():
    return render_template("administration/statistics.html")


@app.route('/administration/user_profiles', methods=['POST', 'GET'])
@login_required
def admin_user_profiles():
    return render_template("administration/user_profiles.html")


@app.route('/administration/virtual_machines', methods=['POST', 'GET'])
@login_required
def admin_virtual_machines():
    return render_template("administration/virtual_machines.html")


@app.route('/administration/workshop_groups', methods=['POST', 'GET'])
@login_required
def admin_workshop_groups():
    return render_template("administration/workshop_groups.html")


@app.route('/administration/workshop_units', methods=['POST', 'GET'])
@login_required
def admin_workshop_units():
    return render_template("administration/workshop_units.html")


@app.route('/users/guest/temporary_workshops', methods=['POST', 'GET'])
@login_required
def users_guest_temporary_workshops():
    return render_template("users/guest/temporary_workshops.html")


@app.route('/users/registered/temporary_workshops', methods=['POST', 'GET'])
@login_required
def users_registered_temporary_workshops():
    return render_template("users/registered/temporary_workshops.html")


@app.route('/users/registered/persistence_workshops', methods=['POST', 'GET'])
@login_required
def users_registered_persistence_workshops():
    return render_template("users/registered/persistence_workshops.html")


if __name__ == "__main__":
    app.run()
