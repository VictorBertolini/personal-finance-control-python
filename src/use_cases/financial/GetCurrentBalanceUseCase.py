from src.model.entities.TransactionType import TransactionType
from src.model.repository.TransactionRepository import TransactionRepository
from decimal import Decimal

class GetCurrentBalanceUseCase:
    def __init__(self, repository: TransactionRepository):
        self.__repository = repository

    def execute(self) -> Decimal:
        transactions = self.__repository.get_all()
        balance = Decimal("0")
        for trans in transactions:
            value = trans.value
            if trans.type == TransactionType.EXPENSE:
                value = trans.value * -1
            balance = balance + value
        return balance
