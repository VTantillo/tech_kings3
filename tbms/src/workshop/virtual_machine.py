"""
A virtual machine will be used by a participant to complete and exercise.  Can
belong to a unit.
"""

from workshop.cloneable import Cloneable


class VirtualMachine(Cloneable):
    """
    A virtual network adapter to connect VMs
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
    # need to put how to clone here too
