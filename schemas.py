from pydantic import BaseModel
from datetime import datetime


class WalletRequest(BaseModel):
    address: str

class WalletResponse(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int
    queried_at: datetime
