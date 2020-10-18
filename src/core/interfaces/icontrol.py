from abc import ABC, abstractmethod


class IControl(ABC):

    @abstractmethod
    def control_impact(self, other):
        """ Sum of control by player or ... non player forces,
         who getting control on actor
        """
        pass
