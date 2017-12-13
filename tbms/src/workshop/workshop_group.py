"""
A workshop group contains multiple workshop units of a specific exercise
"""

from workshop.cloneable import Cloneable
from workshop.portable import Portable
import workshop.workshop_unit


class WorkshopGroup(Cloneable, Portable):
    """
    A collection of WUs of a particular exercise
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