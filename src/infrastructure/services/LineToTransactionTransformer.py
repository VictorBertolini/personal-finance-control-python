from datetime import datetime
from decimal import Decimal

from src.model.entities.Transaction import Transaction
from src.model.entities.TransactionType import TransactionType


class LineToTransactionTransformer:

    def line_to_transaction(self, line: str):
        infos = line.strip().split(",")
        date = infos[5].split("-")
        date = list(map(lambda d: int(d), date))
        return Transaction(int(infos[0].strip()), TransactionType(infos[1].strip()), infos[2].strip(), infos[3].strip(), Decimal(infos[4].strip()), datetime(date[0], date[1], date[2]))

