from flask import render_template


def login_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("login.html", page_error=error_dictionary['page_error'])
    elif 'login_error' in error_dictionary.keys():
        return render_template("login.html", login_error=error_dictionary['login_error'])
    elif 'register_error' in error_dictionary.keys():
        return render_template("login.html", register_error=error_dictionary['register_error'])


def admin_servers_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("administration/servers.html", page_error=error_dictionary['page_error'])


def admin_statistics_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("administration/statistics.html", page_error=error_dictionary['page_error'])


def admin_user_profiles_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("administration/user_profiles.html", page_error=error_dictionary['page_error'])


def admin_virtual_machines_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("administration/virtual_machines.html", page_error=error_dictionary['page_error'])


def admin_workshop_groups_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("administration/workshop_groups.html", page_error=error_dictionary['page_error'])


def admin_workshop_units_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("administration/workshop_units.html", page_error=error_dictionary['page_error'])


def users_guest_temporary_workshops_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("users/guest/temporary_workshops.html", page_error=error_dictionary['page_error'])


def users_registered_temporary_workshops_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("users/registered/temporary_workshops.html", page_error=error_dictionary['page_error'])


def users_registered_persistence_workshops_error(error_dictionary):
    if 'page_error' in error_dictionary.keys():
        return render_template("users/registered/persistence_workshops.html", page_error=error_dictionary['page_error'])