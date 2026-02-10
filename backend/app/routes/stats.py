from fastapi import APIRouter
from app.services.stats_service import get_stats_data
from app.schemas.stats_schema import StatsResponse

router = APIRouter()


@router.get("/stats", response_model=StatsResponse)
def get_stats():
    return get_stats_data()
