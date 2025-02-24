from app.models.stock import Stock
from app.models.training_run import TrainingRun
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class ModelConfig(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    stock_id: int = Field(foreign_key="stock.id", index=True)
    model_name: str = Field(default=None, max_length=50)
    input_size: int = Field(default=1, ge=1)      # e.g., 1 for close price
    num_lstm_layers: int = Field(default=2, ge=1) # e.g., 2 layers
    lstm_size: int = Field(default=32, ge=1)      # e.g., 32 units
    dropout: float = Field(default=0.2, ge=0.0, le=1.0)  # e.g., 0.2
    description: Optional[str] = Field(default=None, max_length=255)

    # Relationships
    stock: "Stock" = Relationship(back_populates="model_configs")
    training_runs: List["TrainingRun"] = Relationship(back_populates="model_config")