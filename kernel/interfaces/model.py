from abc import ABC, abstractmethod

class ModelInterface(ABC):

    """

    Base contract for all AI models connected to AURA.

    """

    @abstractmethod

    def generate(

        self,

        prompt: str,

        context: dict | None = None

    ) -> dict:

        """

        Generate a response.

        """

        pass

    @abstractmethod

    def get_info(self) -> dict:

        """

        Return model information.

        """

        pass

    @abstractmethod

    def health_check(self) -> bool:

        """

        Check if model is available.

        """

        pass