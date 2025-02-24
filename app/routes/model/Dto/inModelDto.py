from pydantic import BaseModel
from typing import Optional

class DefineModelIn(BaseModel):
    model_name: str
    stock_symbol: str
    input_size: int = 1
    num_lstm_layers: int = 2
    lstm_size: int = 32
    dropout: float = 0.2
    description: Optional[str] = None

class TrainModelIn(BaseModel):
    model_id: int
    dataset_id: int
    batch_size: int = 64
    num_epochs: int = 100
    learning_rate: float = 0.01

class EvaluateModelIn(BaseModel):
    training_run_id: int

class PredictModelIn(BaseModel):
    training_run_id: int