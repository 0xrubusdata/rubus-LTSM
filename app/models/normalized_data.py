from app.models.data_point import DataPoint
from app.models.dataset import Dataset
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class NormalizedData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    dataset_id: int = Field(foreign_key="dataset.id", index=True)
    data_point_id: int = Field(foreign_key="datapoint.id", unique=True)  # One-to-one with DataPoint
    normalized_value: float

    # Relationships
    dataset: "Dataset" = Relationship(back_populates="normalized_data")
    data_point: "DataPoint" = Relationship(back_populates="normalized_data")