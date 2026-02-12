from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.services.stats_service import get_stats
from app.schemas.stats_schema import StatsResponse

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
