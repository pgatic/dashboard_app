from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.services.stats_service import get_stats, update_stats
from app.schemas.stats_schema import StatsResponse, StatsUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/stats", response_model=StatsResponse)
def read_stats(db: Session = Depends(get_db)):
    return get_stats(db)


@router.put("/stats", response_model=StatsResponse)
def write_stats(payload: StatsUpdate, db: Session = Depends(get_db)):
    return update_stats(db, payload.users, payload.sales, payload.revenue)
