from src.AppConfig import AppConfig
from src.ui.pages.homepage.Homepage import Homepage
from src.infrastructure.repository.CsvRepository import CsvRepository

def main() -> None:
    repository = CsvRepository("transactions.csv")

    config = AppConfig()
    transaction_controller = config.config_transaction_controller(repository)
    financial_controller = config.config_financial_controller(repository)


    home = Homepage(transaction_controller, financial_controller)
    home.initialize()
    home.menu()

if __name__ == "__main__":
    main()