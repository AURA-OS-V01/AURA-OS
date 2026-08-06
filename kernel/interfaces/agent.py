from abc import ABC, abstractmethod

class AgentInterface(ABC):

    """

    Base contract for all AURA agents.

    """

    def __init__(self, name: str):

        self.name = name

    @abstractmethod

    def process(self, input_data: dict) -> dict:

        """

        Main agent processing function.

        """

        pass

    @abstractmethod

    def get_status(self) -> dict:

        """

        Returns agent health/status.

        """

        pass