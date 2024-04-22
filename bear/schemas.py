from typing import Literal
from pydantic import BaseModel, ValidationError
from datetime import date
from decimal import Decimal


class CreatePlayer(BaseModel):
    name: str
    document: str
    phone: str
    date_birth: date

class CreateWithdraw(BaseModel):
    value : Decimal
    player_id: int

class CreateDeposit(BaseModel):
    value: Decimal
    player_id: int