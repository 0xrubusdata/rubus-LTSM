from app.models.normalized_data import NormalizedData
from app.models.stock import Stock
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date

class DataPoint(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    stock_id: int = Field(foreign_key="stock.id", index=True)
    date: date = Field(index=True)           # Date of the price
    adjusted_close: float                    # Raw adjusted close price

    # Relationship
    stock: "Stock" = Relationship(back_populates="data_points")
    normalized_data: Optional["NormalizedData"] = Relationship(back_populates="data_point")