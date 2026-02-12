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
            {
                "day": item.day,
                "sales": item.sales,
            }
            for item in stats.history
        ],
    }
