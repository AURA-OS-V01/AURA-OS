from abc import ABC, abstractmethod

class MemoryInterface(ABC):

    """

    Base contract for all AURA memory systems.

    """

    @abstractmethod

    def store(self, key: str, value: dict) -> bool:

        """

        Store information.

        """

        pass

    @abstractmethod

    def retrieve(self, key: str) -> dict | None:

        """

        Retrieve information.

        """

        pass

    @abstractmethod

    def delete(self, key: str) -> bool:

        """

        Remove information.

        """

        pass

    @abstractmethod

    def search(self, query: str) -> list:

        """

        Search memory.

        """

        pass