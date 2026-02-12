from sqlalchemy.orm import Session
from app.models.stats import Stats


def get_stats(db: Session):
    stats = db.query(Stats).first()

    if not stats:
        return None

    return {
        "users": stats.users,
        "sales": stats.sales,
        "revenue": stats.revenue,
        "sales_history": [
            {"day": "Mon", "sales": 5},
            {"day": "Tue", "sales": 8},
            {"day": "Wed", "sales": 6},
            {"day": "Thu", "sales": 10},
            {"day": "Fri", "sales": 6},
        ],
    }
