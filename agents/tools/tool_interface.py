from abc import ABC, abstractmethod

class ToolInterface(ABC):

    """

    Base interface for AURA tools.

    """

    def __init__(

        self,

        name: str

    ):

        self.name = name

    @abstractmethod

    def execute(

        self,

        input_data

    ):

        pass