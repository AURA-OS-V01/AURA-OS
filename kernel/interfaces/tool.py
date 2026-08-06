from abc import ABC, abstractmethod

class ToolInterface(ABC):

    """

    Base contract for all AURA tools.

    """

    @abstractmethod

    def execute(self, parameters: dict) -> dict:

        """

        Execute the tool action.

        """

        pass

    @abstractmethod

    def get_name(self) -> str:

        """

        Return tool name.

        """

        pass

    @abstractmethod

    def get_description(self) -> str:

        """

        Explain what the tool does.

        """

        pass

    @abstractmethod

    def health_check(self) -> bool:

        """

        Check if the tool is working.

        """

        pass