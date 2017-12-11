"""
A workshop unit contains multiple virtual machines for a particular exercise
"""

from workshop.cloneable import Cloneable
from workshop.portable import Portable


class WorkshopUnit(Cloneable, Portable):
    """
    A collection of VMs of a particular exercise
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
    # clone and port stuff here too
