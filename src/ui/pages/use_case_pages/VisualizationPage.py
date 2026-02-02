from src.controllers.FinancialController import FinancialController
from src.controllers.TransactionController import TransactionController
from src.model.entities.Transaction import Transaction


class VisualizationPage:

    line_size = 110

    def __init__(self, transaction_controller: TransactionController, financial_controller: FinancialController):
        self.transaction_controller = transaction_controller
        self.financial_controller = financial_controller

    def initialize(self):
        while True:
            self.menu()
            try:
                option = int(input("Select one option: "))
                match option:
                    case 1: # All
                        trans = self.transaction_controller.get_all_transactions()
                        self.__show_transactions(trans)

                    case 2: # By Month
                        month_dict = self.financial_controller.filter_transactions_by_month()
                        print("=" * self.line_size)
                        if not month_dict:
                            print("No transactions found")
                            continue

                        for month, transactions in month_dict.items():
                            print("-" * self.line_size)
                            print(f"MONTH: {month}")
                            if not transactions:
                                print("(empty)")
                            else:
                                self.__show_transactions(transactions)


                    case 3: # Specific month
                        target_month = self.__get_target_month()
                        transactions = self.financial_controller.filter_transactions_by_month_number(target_month)
                        self.__show_transactions(transactions)

                    case 4: # By category
                        categories_dict = self.financial_controller.filter_transactions_by_category()
                        print("=" * self.line_size)
                        if not categories_dict:
                            print("No transactions found")
                            continue

                        for category, transactions in categories_dict.items():
                            print("-" * self.line_size)
                            print(f"CATEGORY: {category.upper()}")
                            if not transactions:
                                print("(empty)")
                            else:
                                self.__show_transactions(transactions)

                    case 5: # By specific category
                        category = self.__get_target_category()
                        transactions = self.financial_controller.filter_transactions_by_single_category(category)
                        if not transactions:
                            print("No transactions found for this category.")
                            continue
                        self.__show_transactions(transactions)

                    case 6: # By Category in a month
                        month_number = self.__get_target_month()
                        category = self.__get_target_category()
                        transactions = self.financial_controller.filter_transactions_by_category_in_month(month_number, category)
                        if not transactions:
                            print("No transactions found for this month/category.")
                            continue
                        self.__show_transactions(transactions)

                    case 7: # Single
                        target_id = self.__get_target_id()
                        transaction = self.transaction_controller.get_transaction_by_id(target_id)
                        if transaction is None:
                            print("Invalid Id")
                            continue
                        self.__show_transactions([transaction])

                    case 9:
                        return

                    case _:
                        print("Invalid Option")
            except:
                print("Invalid Option!")


    def menu(self):
        print("=" * self.line_size)
        print("How do you want to view?")
        print("1. Visualize all transactions")
        print("2. Visualize all transactions by month")
        print("3. Visualize all of a specific month")
        print("4. Visualize all transactions by category")
        print("5. Visualize all by specific category")
        print("6. Visualize all of a specific categoria in a specific month")
        print("7. Visualize a single transaction")
        print("9. Back")

    def __get_target_month(self):
        print("=" * self.line_size)
        while True:
            try:
                month_number = int(input("Enter the month number: "))
                if not 1 <= month_number <= 12:
                    raise Exception("Invalid, month must be between 1 and 12")
                return month_number
            except:
                print("Invalid, enter a valid month number")

    def __get_target_category(self) -> str:
        print("=" * self.line_size)
        while True:
            try:
                category = str(input("Enter the category: "))
                if category == "":
                    raise Exception
                return category.upper()
            except:
                print("Invalid, enter a valid category")

    def __get_target_id(self) -> int:
        print("=" * self.line_size)
        while True:
            try:
                target_id = int(input("Enter the transaction id: "))
                if target_id <= 0:
                    raise Exception("Invalid, id can't be 0 or lower")
                return target_id
            except:
                print("Invalid, enter a valid id")

    def __show_transactions(self, transactions: list[Transaction]):
        print("=" * self.line_size)

        header = (
            f"{'ID':<4} "
            f"{'DATE':<12} "
            f"{'TYPE':<8} "
            f"{'CATEGORY':<15} "
            f"{'DESCRIPTION':<40} "
            f"{'VALUE':>10}"
        )
        print(header)
        print("-" * self.line_size)

        for transaction in transactions:
            self.__show_transaction(transaction)

        print("=" * self.line_size)

    def __show_transaction(self, transaction: Transaction):
        category = self.__truncate(transaction.category, 15)
        description = self.__truncate(transaction.description, 40)

        date_str = transaction.date.strftime("%Y-%m-%d")
        value_str = f"{transaction.value:.2f}"

        print(
            f"{transaction.id:<4} "
            f"{date_str:<12} "
            f"{transaction.type.value:<8} "
            f"{category:<15} "
            f"{description:<40} "
            f"{value_str:>10}"
        )

    def __truncate(self, text: str, max_len: int) -> str:
        if len(text) <= max_len:
            return text
        return text[: max_len - 3] + "..."