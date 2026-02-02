from src.model.entities.Transaction import Transaction
from src.model.repository.TransactionRepository import TransactionRepository


class FilterTransactionsUseCase:

    def __init__(self, repository: TransactionRepository):
        self.__repository = repository

    def execute_by_month(self) -> dict[int, list[Transaction]]:
        transactions = self.__repository.get_all() or []

        month_dict = {
            1: [], 2: [], 3: [], 4: [], 5: [], 6: [],
            7: [], 8: [], 9: [], 10: [], 11: [], 12: []
        }

        for trans in transactions:
            month_dict[trans.date.month].append(trans)

        return month_dict

    def execute_by_month_number(self, month_number: int) -> list[Transaction]:
        transactions = self.__repository.get_all()

        month_list = []

        if not 1 <= month_number <= 12:
            return []

        for trans in transactions:
            if trans.date.month == month_number:
                month_list.append(trans)

        return month_list

    def execute_by_category(self) -> dict[str, list[Transaction]]:
        transactions = self.__repository.get_all() or []

        category_dict: dict[str, list] = {}

        for trans in transactions:
            if trans.category not in category_dict:
                category_dict[trans.category] = []
            category_dict[trans.category].append(trans)

        return category_dict

    def execute_by_single_category(self, target_category: str) -> list[Transaction]:
        transactions = self.__repository.get_all() or []

        category_list = []

        for trans in transactions:
            if trans.category.upper() == target_category.upper():
                category_list.append(trans)
        return category_list

    def execute_by_category_in_month(self, target_month: int, target_category: str) -> list[Transaction]:
        transactions = self.execute_by_month_number(target_month)

        category_list = []
        for trans in transactions:
            if trans.category.upper() == target_category.upper():
                category_list.append(trans)
        return category_list
