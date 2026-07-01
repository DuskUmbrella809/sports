from abc import ABC, abstractmethod

from sports.models import Match


class BaseProvider(ABC):
    @abstractmethod
    def get_matches(self) -> list[Match]:
        """Return the current matches."""
        raise NotImplementedError