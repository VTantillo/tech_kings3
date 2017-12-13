"""
Specifies actions that a user may take in the system.
Specified by method calls.
"""


class Permissions:
    """
    Base class for actions a user can take in the system.
    """

    def __init__(self):
        pass

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    # private responsibilities go here


class Participant(Permissions):
    """
    Actions that a participant can make in the system.
    Includes guests, and registered participants
    """

    # Actions that a participant go here


class Authenticated(Permissions):
    """
    Actions that a user can make who signs in

    Includes registered participants and administrators
    """

    # Actions of authenticated users go here


class Administrator(Authenticated):
    """
    Actions that an administrator can do.
    """

    # Admin actions


class Registered(Authenticated, Participant):
    """
    Actions that a registered participant can do.
    """

    # Registered participant


class Guest(Participant):
    """
    Actions that a guest participant can do.
    """

    # Guest participant actions
