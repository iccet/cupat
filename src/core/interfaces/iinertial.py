from abc import ABC, abstractmethod


class IInertial(ABC):

    @abstractmethod
    def inertial_impact(self):
        """ Sum of all actor inertial force momentum """
        pass
