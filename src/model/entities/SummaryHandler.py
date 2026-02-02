from abc import ABC, abstractmethod

class SummaryHandler(ABC):
    @abstractmethod
    def show_summary(self) -> None:
        ...