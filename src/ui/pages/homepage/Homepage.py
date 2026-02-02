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
        print("BEM VINDO AO")
        print("CONTROLE DE FINANÇAS PESSOAIS")

    def menu(self):
        while True:
            print("=" * self.line_size)
            print("Options:")
            print("1. Inserir uma transação")
            print("2. Remover uma transação")
            print("3. Visualizar transações")
            print("4. Ver saldo atual")
            print("5. Gerar relatório")
            print("9. Sair")

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







