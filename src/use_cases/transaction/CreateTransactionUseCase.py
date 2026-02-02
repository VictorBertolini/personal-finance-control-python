from datetime import datetime
from decimal import Decimal

from src.model.entities.Transaction import Transaction
from src.model.entities.TransactionType import TransactionType
from src.model.repository.TransactionRepository import TransactionRepository

class CreateTransactionUseCase:
    __repository: TransactionRepository

    def __init__(self, repository: TransactionRepository):
        self.__repository = repository

    def execute(self, transaction_type: TransactionType, category: str, description: str, value: Decimal, date: datetime) -> int:
        new_id = self.__repository.get_last_id() + 1
        transaction = Transaction(new_id, transaction_type, category, description, value, date)
        return self.__repository.create(transaction)
