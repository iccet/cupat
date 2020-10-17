from abc import ABC, abstractmethod


class IDynamic(ABC):

    @abstractmethod
    def update(self):
        pass
