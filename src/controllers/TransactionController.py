from typing import List

from src.controllers.dto.TransactionDTO import TransactionDTO
from src.model.entities.Transaction import Transaction
from src.use_cases.transaction.CreateTransactionUseCase import CreateTransactionUseCase
from src.use_cases.transaction.DeleteTransactionUseCase import DeleteTransactionUseCase
from src.use_cases.transaction.GetTransactionUseCase import GetTransactionUseCase


class TransactionController:
    def __init__(self, create_transaction_use_case: CreateTransactionUseCase, delete_transaction_use_case: DeleteTransactionUseCase, get_transaction_use_case: GetTransactionUseCase):
        self.__create_transaction_use_case = create_transaction_use_case
        self.__delete_transaction_use_case = delete_transaction_use_case
        self.__get_transaction_use_case = get_transaction_use_case


    def create_transaction(self, transaction_dto: TransactionDTO) -> int:
        return self.__create_transaction_use_case.execute(transaction_dto.type, transaction_dto.category, transaction_dto.description, transaction_dto.value, transaction_dto.date)

    def delete_transaction(self, id: int) -> bool:
        return self.__delete_transaction_use_case.execute(id)

    def get_all_transactions(self) -> List[Transaction]:
        return self.__get_transaction_use_case.execute()

    def get_transaction_by_id(self, id: int) -> Transaction | None:
        return self.__get_transaction_use_case.execute_by_id(id)
