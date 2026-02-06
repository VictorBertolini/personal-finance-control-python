import os.path, os

from src.model.entities.Transaction import Transaction
from src.model.repository.TransactionRepository import TransactionRepository
from src.infrastructure.services.LineToTransactionTransformer import LineToTransactionTransformer

class CsvRepository(TransactionRepository):
    def __init__(self, file_name: str):
        self.file_name = "../data/" + file_name
        os.makedirs("../data", exist_ok=True)
        if not os.path.exists(self.file_name):
            open(self.file_name, mode="w" ,encoding="utf-8").close()

    def get_last_id(self) -> int:
        transactions = self.get_all()
        last_id = 0
        for trans in transactions:
            if trans.id > last_id:
                last_id = trans.id
        return last_id

    def delete(self, id: int) -> bool:
        transactions = self.get_all()
        for trans in transactions:
            if trans.id == id:
                transactions.remove(trans)
                self.create_all(transactions)
                return True
        return False

    def create(self, transaction: Transaction) -> int:
        line = f"{transaction.id},{transaction.type.value},{transaction.category.upper()},{transaction.description},{transaction.value},{transaction.date.date()}\n"
        with open(self.file_name, mode="a", encoding="utf-8") as repository:
            repository.write(line)
        return transaction.id
    
    def create_all(self, transactions: list[Transaction]) -> None:
        with open(self.file_name, mode="w", encoding="utf-8") as repository:
            for transaction in transactions:
                line = f"{transaction.id},{transaction.type.value},{transaction.category.upper()},{transaction.description},{transaction.value},{transaction.date.date()}\n"
                repository.write(line)
            
    def get_transaction(self, target_id: int) -> Transaction | None:
        transactions = self.get_all()
        for trans in transactions:
            if trans.id == target_id:
                return trans
        return None

    def get_all(self) -> list[Transaction]:
        transformer = LineToTransactionTransformer()
        with open(self.file_name, mode="r", encoding="utf-8") as repository:
            transactions = repository.readlines()

        if not transactions:
            return []
        return list(map(lambda t: transformer.line_to_transaction(t), transactions))
