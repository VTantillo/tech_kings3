from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def login():
    return render_template("login.html")


@app.route('/administration/servers', methods=['POST', 'GET'])
def admin_servers():
    return render_template("administration/servers.html")


@app.route('/administration/statistics', methods=['POST', 'GET'])
def admin_statistics():
    return render_template("administration/statistics.html")


@app.route('/administration/user_profiles', methods=['POST', 'GET'])
def admin_user_profiles():
    return render_template("administration/user_profiles.html")


@app.route('/administration/virtual_machines', methods=['POST', 'GET'])
def admin_virtual_machines():
    return render_template("administration/virtual_machines.html")


@app.route('/administration/workshop_groups', methods=['POST', 'GET'])
def admin_workshop_groups():
    return render_template("administration/workshop_groups.html")


@app.route('/administration/workshop_units', methods=['POST', 'GET'])
def admin_workshop_units():
    return render_template("administration/workshop_units.html")


@app.route('/users/guest/temporary_workshops', methods=['POST', 'GET'])
def users_guest_temporary_workshops():
    return render_template("users/guest/temporary_workshops.html")


@app.route('/users/registered/temporary_workshops', methods=['POST', 'GET'])
def users_registered_temporary_workshops():
    return render_template("users/registered/temporary_workshops.html")


@app.route('/users/registered/persistence_workshops', methods=['POST', 'GET'])
def users_registered_persistence_workshops():
    return render_template("users/registered/persistence_workshops.html")


if __name__ == "__main__":
    app.run()
