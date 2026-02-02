from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from src.model.entities.TransactionType import TransactionType

@dataclass
class TransactionDTO:
    type: TransactionType
    category: str
    description: str
    value: Decimal
    date: datetime
