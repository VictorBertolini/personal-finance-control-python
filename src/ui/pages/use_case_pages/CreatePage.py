from datetime import datetime
from decimal import Decimal

from src.controllers.TransactionController import TransactionController
from src.controllers.dto.TransactionDTO import TransactionDTO
from src.model.entities.TransactionType import TransactionType


class CreatePage:

    line_size = 25

    def __init__(self, transaction_controller: TransactionController):
        self.transaction_controller = transaction_controller

    def create_transaction(self):
        transaction_dto = self.transaction_input()
        self.transaction_controller.create_transaction(transaction_dto)

    def transaction_input(self) -> TransactionDTO:
        transaction_type = self.__get_type()
        category = self.__get_category()
        description = self.__get_description()
        value = self.__get_value()
        date = self.__get_date()

        return TransactionDTO(transaction_type, category, description, value, date)

    def __get_type(self) -> TransactionType:
        while True:
            print("=" * self.line_size)
            print("What type is this transaction?")
            print("1. Income")
            print("2. Expense")
            try:
                option = int(input(":"))

                match option:
                    case 1:
                        return TransactionType.INCOME
                    case 2:
                        return TransactionType.EXPENSE
                    case _:
                        print("Invalid option, try again")
            except ValueError:
                print("Invalid option, try again")

    def __get_category(self) -> str:
        while True:
            print("=" * self.line_size)
            print("Enter the category of the transaction")
            option = input(":")
            if option == "":
                print("Invalid, category could not be blank")
                continue
            else:
                break
        return option.upper()

    def __get_description(self) -> str | None:
        print("=" * self.line_size)
        print("Enter a description in the transaction")
        option = input(":")

        return option

    def __get_value(self) -> Decimal:
        while True:
            print("=" * self.line_size)
            print("Enter the transaction value")
            option = input("$")
            try:
                option = Decimal(option)
                if option <= 0:
                    raise Exception("Value could not be negative or zero")
                break
            except:
                print("Invalid, value must be like 1234.56")

        return option

    def __get_date(self) -> datetime:
        while True:
            try:
                print("=" * self.line_size)
                day = int(input("Enter the day of the transaction: "))
                month = int(input("Enter the month of the transaction: "))
                year = int(input("Enter the year of the transaction: "))

                date = datetime(year, month, day)

                return date
            except Exception as e:
                print(f"Invalid, {e}")