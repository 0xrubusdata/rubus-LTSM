from app.models.training_run import TrainingRun
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date

class Prediction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    training_run_id: int = Field(foreign_key="trainingrun.id", index=True)
    date: date = Field(index=True)             # Date being predicted
    actual_price: Optional[float] = None       # Known price (null if future)
    predicted_price: float                     # Model’s prediction

    # Relationship
    training_run: "TrainingRun" = Relationship(back_populates="predictions")