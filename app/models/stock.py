from app.models.data_point import DataPoint
from app.models.dataset import Dataset
from app.models.model_config import ModelConfig
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Stock(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    symbol: str = Field(max_length=10, unique=True, index=True)  # e.g., "IBM"
    name: Optional[str] = Field(default=None, max_length=100)    # e.g., "International Business Machines"

    # Relationships
    data_points: List["DataPoint"] = Relationship(back_populates="stock")
    datasets: List["Dataset"] = Relationship(back_populates="stock")
    model_configs: List["ModelConfig"] = Relationship(back_populates="stock")