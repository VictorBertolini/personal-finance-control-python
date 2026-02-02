from src.model.entities.Transaction import Transaction
from src.model.repository.TransactionRepository import TransactionRepository


class GetTransactionUseCase:
    __repository: TransactionRepository

    def __init__(self, repository: TransactionRepository):
        self.__repository = repository

    def execute(self) -> list[Transaction]:
        return self.__repository.get_all()

    def execute_by_id(self, id: int) -> Transaction | None:
        return self.__repository.get_transaction(id)
