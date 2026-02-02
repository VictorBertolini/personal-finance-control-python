from decimal import Decimal

from src.model.entities.SummaryHandler import SummaryHandler
from src.model.entities.TransactionType import TransactionType

from src.use_cases.financial.FilterTransactionsUseCase import FilterTransactionsUseCase


class SummaryTerminalStyler(SummaryHandler):
    def __init__(self, filter_transaction: FilterTransactionsUseCase):
        self.__filter_transactions = filter_transaction
        self.__line_size = 55

    def show_summary(self) -> None:
        month_dict = self.__filter_transactions.execute_by_month()
        overall_income = Decimal("0")
        overall_expense = Decimal("0")

        print("=" * self.__line_size)
        print("FINANCIAL SUMMARY (MONTHLY)")
        print("=" * self.__line_size)
        print(f"{'Month':<8}{'Income':>14}{'Expense':>14}{'Net':>14}")
        print("-" * self.__line_size)

        for month in range(1, 13):
            transactions = month_dict.get(month, [])

            income = Decimal("0")
            expense = Decimal("0")

            for t in transactions:
                if t.type == TransactionType.INCOME:
                    income += t.value
                else:
                    expense += t.value

            net = income - expense
            overall_income += income
            overall_expense += expense

            print(f"{month:02d}/{'':<5}{income:>14}{expense:>14}{net:>14}")

        print("-" * self.__line_size)
        overall_net = overall_income - overall_expense
        print(f"{'TOTAL':<8}{overall_income:>14}{overall_expense:>14}{overall_net:>14}")
        print("=" * self.__line_size)

