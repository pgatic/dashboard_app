from pydantic import BaseModel


class StatsResponse(BaseModel):
    users: int
    sales: int
    revenue: int
