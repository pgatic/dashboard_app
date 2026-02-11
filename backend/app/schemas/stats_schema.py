from pydantic import BaseModel
from typing import List


class StatsResponse(BaseModel):
    users: int
    sales: int
    revenue: int
    sales_history: List[int]
