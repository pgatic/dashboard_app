from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db import Base
from app.main import app
from app.models.sales_history import SalesHistory
from app.models.stats import Stats
from app.routes.stats import get_db


engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def seed_test_data():
    db = TestingSessionLocal()
    try:
        stats = Stats(users=120, sales=35, revenue=5400)
        db.add(stats)
        db.commit()
        db.refresh(stats)
        db.add(SalesHistory(day="Mon", sales=5, stats_id=stats.id))
        db.commit()
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
seed_test_data()
client = TestClient(app)


def test_get_stats_returns_json():
    response = client.get("/api/stats")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")


def test_put_stats_updates_values():
    payload = {"users": 150, "sales": 42, "revenue": 7200}

    response = client.put("/api/stats", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["users"] == payload["users"]
    assert data["sales"] == payload["sales"]
    assert data["revenue"] == payload["revenue"]
