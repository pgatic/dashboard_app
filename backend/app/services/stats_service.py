from sqlalchemy.orm import Session
from app.models.stats import Stats


def format_stats_response(stats: Stats):
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


def get_stats(db: Session):
    stats = db.query(Stats).first()

    if not stats:
        return None

    return format_stats_response(stats)


def update_stats(db: Session, users: int, sales: int, revenue: int):
    stats = db.query(Stats).first()

    if not stats:
        stats = Stats(users=users, sales=sales, revenue=revenue)
        db.add(stats)
    else:
        stats.users = users
        stats.sales = sales
        stats.revenue = revenue

    db.commit()
    db.refresh(stats)

    return format_stats_response(stats)
