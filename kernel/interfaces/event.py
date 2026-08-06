from abc import ABC, abstractmethod

class EventInterface(ABC):

    """

    Base contract for AURA event systems.

    """

    @abstractmethod

    def publish(self, event) -> bool:

        """

        Send an event through the system.

        """

        pass

    @abstractmethod

    def subscribe(self, event_type: str, handler) -> bool:

        """

        Listen for a specific event type.

        """

        pass

    @abstractmethod

    def unsubscribe(self, event_type: str, handler) -> bool:

        """

        Remove an event listener.

        """

        pass