from src.model.entities.Transaction import Transaction
from abc import ABC, abstractmethod

class TransactionRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Transaction]:
        ...

    @abstractmethod
    def get_transaction(self, id: int) -> Transaction | None:
        ...

    @abstractmethod
    def create(self, transaction: Transaction) -> int:
        ...

    @abstractmethod
    def delete(self, id: int) -> bool:
        ...

    @abstractmethod
    def get_last_id(self) -> int:
        ...
