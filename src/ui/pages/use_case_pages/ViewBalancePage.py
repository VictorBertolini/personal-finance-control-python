from src.controllers.FinancialController import FinancialController


class ViewBalancePage:
    def __init__(self, financial_controller: FinancialController):
        self.financial_controller = financial_controller

    def view_balance(self):
        value = self.financial_controller.get_current_balance()
        print(f"The current balance is: ${value}")


