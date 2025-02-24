from app.models.dataset import Dataset
from app.models.model_config import ModelConfig
from app.models.prediction import Prediction
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class TrainingRun(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_config_id: int = Field(foreign_key="modelconfig.id", index=True)
    dataset_id: int = Field(foreign_key="dataset.id", index=True)
    batch_size: int = Field(ge=1)              # e.g., 64
    num_epochs: int = Field(ge=1)              # e.g., 100
    learning_rate: float = Field(gt=0.0)       # e.g., 0.01
    train_loss: Optional[float] = None         # Final training loss
    val_loss: Optional[float] = None           # Final validation loss
    started_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    model_state_path: Optional[str] = Field(default=None, max_length=255)  # e.g., "/models/run_1.pth"

    # Relationships
    model_config: "ModelConfig" = Relationship(back_populates="training_runs")
    dataset: "Dataset" = Relationship(back_populates="training_runs")
    predictions: List["Prediction"] = Relationship(back_populates="training_run")