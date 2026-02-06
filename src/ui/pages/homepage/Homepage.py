from src.controllers.FinancialController import FinancialController
from src.controllers.TransactionController import TransactionController
from src.ui.pages.use_case_pages.CreatePage import CreatePage
from src.ui.pages.use_case_pages.DeletePage import DeletePage
from src.ui.pages.use_case_pages.ViewBalancePage import ViewBalancePage
from src.ui.pages.use_case_pages.VisualizationPage import VisualizationPage


class Homepage:
    line_size: int = 25

    def __init__(self, transaction_controller: TransactionController, financial_controller: FinancialController):
        self.transaction_controller = transaction_controller
        self.financial_controller = financial_controller

    def initialize(self):
        print("=" * self.line_size)
        print("WELCOME TO")
        print("PERSONAL FINANCE CONTROL")

    def menu(self):
        while True:
            print("=" * self.line_size)
            print("Options:")
            print("1. Insert a new Transaction")
            print("2. Remove a Transaction")
            print("3. Visualize Transactions")
            print("4. Check current balance")
            print("5. Generate Summary")
            print("9. Exit")

            try:
                option = int(input("Choose one: "))

                match option:
                    case 1:
                        CreatePage(self.transaction_controller).create_transaction()
                    case 2:
                        DeletePage(self.transaction_controller).delete_page()
                    case 3:
                        VisualizationPage(self.transaction_controller, self.financial_controller).initialize()
                    case 4:
                        ViewBalancePage(self.financial_controller).view_balance()
                    case 5:
                        self.financial_controller.show_financial_summary()
                    case 9:
                        print("Bye")
                        break
                    case _:
                        print("Invalid option!")
            except:
                print("Invalid option!")







