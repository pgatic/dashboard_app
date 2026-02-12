from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class SalesHistory(Base):
    __tablename__ = "sales_history"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(String, nullable=False)
    sales = Column(Integer, nullable=False)

    stats_id = Column(Integer, ForeignKey("stats.id"))

    stats = relationship("Stats", back_populates="history")
