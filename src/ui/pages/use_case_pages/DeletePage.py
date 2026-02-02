from src.controllers.TransactionController import TransactionController
from src.model.entities.Transaction import Transaction


class DeletePage:
    line_size = 110

    def __init__(self, transaction_controller: TransactionController):
        self.transaction_controller = transaction_controller

    def delete_page(self):
        self.__show_transactions(self.transaction_controller.get_all_transactions())
        target_id = self.__select_transaction_id()
        deleted = self.transaction_controller.delete_transaction(target_id)
        if not deleted:
            print("Invalid operation! Id not exist")

    def __select_transaction_id(self) -> int:
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