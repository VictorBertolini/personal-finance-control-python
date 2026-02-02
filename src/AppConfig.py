from src.controllers.FinancialController import FinancialController
from src.controllers.TransactionController import TransactionController
from src.model.repository.TransactionRepository import TransactionRepository
from src.ui.summary.SummaryTerminalStyler import SummaryTerminalStyler
from src.use_cases.financial.GetCurrentBalanceUseCase import GetCurrentBalanceUseCase
from src.use_cases.financial.FilterTransactionsUseCase import FilterTransactionsUseCase
from src.use_cases.financial.GetFinancialSummaryUseCase import GetFinancialSummaryUseCase
from src.use_cases.transaction.CreateTransactionUseCase import CreateTransactionUseCase
from src.use_cases.transaction.DeleteTransactionUseCase import DeleteTransactionUseCase
from src.use_cases.transaction.GetTransactionUseCase import GetTransactionUseCase


class AppConfig:
    def config_transaction_controller(self, repository: TransactionRepository) -> TransactionController:
        create = CreateTransactionUseCase(repository)
        delete = DeleteTransactionUseCase(repository)
        get = GetTransactionUseCase(repository)

        return TransactionController(create, delete, get)

    def config_financial_controller(self, repository: TransactionRepository) -> FinancialController:
        get_current_balance = GetCurrentBalanceUseCase(repository)
        get_summary = FilterTransactionsUseCase(repository)
        get_financial_summary = GetFinancialSummaryUseCase(SummaryTerminalStyler(get_summary))

        return FinancialController(get_current_balance, get_summary, get_financial_summary)



