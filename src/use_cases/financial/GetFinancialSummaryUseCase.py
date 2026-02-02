from src.model.entities.SummaryHandler import SummaryHandler


class GetFinancialSummaryUseCase:

    def __init__(self, summary_handler: SummaryHandler):
        self.__summary_handler = summary_handler

    def execute(self) -> None:
        self.__summary_handler.show_summary()
