from datetime import datetime
from decimal import Decimal
from dataclasses import dataclass

from src.model.entities.TransactionType import TransactionType

@dataclass
class Transaction:
    id: int
    type: TransactionType
    category: str
    description: str
    value: Decimal
    date: datetime

    def __post_init__(self):
        if self.id < 1:
            raise ValueError("transaction id can't be lower than 1")
        if self.value <= 0:
            raise ValueError("transaction value can't be 0 or lower")
