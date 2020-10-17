from abc import ABC, abstractmethod


class IRender(ABC):

    @abstractmethod
    def render(self):
        pass
