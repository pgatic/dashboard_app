from fastapi import FastAPI
from app.routes.stats import router as stats_router
from fastapi.middleware.cors import CORSMiddleware

from app.db import engine, Base
#from app.models import stats

from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.stats import Stats
from app.models import sales_history
from app.models.sales_history import SalesHistory

app = FastAPI()

Base.metadata.create_all(bind=engine)

def seed_data():
    db: Session = SessionLocal()
    try:
        existing = db.query(Stats).first()

        if not existing:
            new_stats = Stats(users=120, sales=35, revenue=5400)
            db.add(new_stats)
            db.commit()
            db.refresh(new_stats)

            history_items = [
                SalesHistory(day="Mon", sales=5, stats_id=new_stats.id),
                SalesHistory(day="Tue", sales=8, stats_id=new_stats.id),
                SalesHistory(day="Wed", sales=6, stats_id=new_stats.id),
                SalesHistory(day="Thu", sales=10, stats_id=new_stats.id),
                SalesHistory(day="Fri", sales=6, stats_id=new_stats.id),
            ]

            db.add_all(history_items)
            db.commit()

    finally:
        db.close()


seed_data()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only; production: allow_origins=["https://tvoj-frontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(stats_router, prefix="/api")
