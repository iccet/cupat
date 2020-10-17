from abc import ABC, abstractmethod


class IImpact(ABC):

    @abstractmethod
    def impact_on(self, other):
        """ Impact ON external objects """
        pass

