from src.model.entities.Transaction import Transaction
from src.use_cases.financial.GetCurrentBalanceUseCase import GetCurrentBalanceUseCase
from src.use_cases.financial.FilterTransactionsUseCase import FilterTransactionsUseCase
from decimal import Decimal

from src.use_cases.financial.GetFinancialSummaryUseCase import GetFinancialSummaryUseCase


class FinancialController:

    def __init__(self, get_current_balance_use_case: GetCurrentBalanceUseCase, filter_transactions_use_case: FilterTransactionsUseCase, financial_summary_use_case: GetFinancialSummaryUseCase):
        self.__get_current_balance_use_case = get_current_balance_use_case
        self.__filter_transactions_use_case = filter_transactions_use_case
        self.__financial_summary_use_case = financial_summary_use_case

    def get_current_balance(self) -> Decimal:
        return self.__get_current_balance_use_case.execute()

    def filter_transactions_by_month(self) -> dict[int, list[Transaction]]:
        return self.__filter_transactions_use_case.execute_by_month()

    def filter_transactions_by_month_number(self, number: int) -> list[Transaction]:
        return self.__filter_transactions_use_case.execute_by_month_number(number)

    def filter_transactions_by_category(self) -> dict[str, list[Transaction]]:
        return self.__filter_transactions_use_case.execute_by_category()

    def filter_transactions_by_single_category(self, category: str) -> list[Transaction]:
        return self.__filter_transactions_use_case.execute_by_single_category(category)

    def filter_transactions_by_category_in_month(self, month: int, category: str) -> list[Transaction]:
        return self.__filter_transactions_use_case.execute_by_category_in_month(month, category)

    def show_financial_summary(self):
        self.__financial_summary_use_case.execute()

