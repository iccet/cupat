from abc import ABC, abstractmethod


class IInCollision(ABC):

    @abstractmethod
    def in_collision(self, other):
        """ Impact OF external objects """
        pass
