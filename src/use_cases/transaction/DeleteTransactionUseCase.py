from src.model.repository.TransactionRepository import TransactionRepository

class DeleteTransactionUseCase:
    __repository: TransactionRepository

    def __init__(self, repository: TransactionRepository):
        self.__repository = repository

    def execute(self, id: int) -> bool:
        return self.__repository.delete(id)
