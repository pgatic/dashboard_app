from pydantic import BaseModel
from typing import List


class SalesHistoryItem(BaseModel):
    day: str
    sales: int


class StatsResponse(BaseModel):
    users: int
    sales: int
    revenue: int
    sales_history: List[SalesHistoryItem]
