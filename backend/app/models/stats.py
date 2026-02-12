from sqlalchemy import Column, Integer
from app.db import Base


class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True)
    users = Column(Integer, nullable=False)
    sales = Column(Integer, nullable=False)
    revenue = Column(Integer, nullable=False)
