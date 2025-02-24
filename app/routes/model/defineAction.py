from app.main import get_session
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import Stock, ModelConfig
from app.routes.model.Dto.inModelDto import DefineModelIn
from app.routes.model.Dto.outModelDto import ModelConfigOut

router = APIRouter()

@router.post("/define", response_model=ModelConfigOut, description="Defines an LSTM model configuration for a given stock.")
def define_model(data_in: DefineModelIn, session: Session = Depends(get_session)):
    # Check if stock exists
    stock = session.exec(select(Stock).where(Stock.symbol == data_in.stock_symbol)).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")
    
    model_config = ModelConfig(
        stock_id=stock.id,
        model_name=data_in.model_name,
        input_size=data_in.input_size,
        num_lstm_layers=data_in.num_lstm_layers,
        lstm_size=data_in.lstm_size,
        dropout=data_in.dropout,
        description=data_in.description
    )
    session.add(model_config)
    session.commit()
    session.refresh(model_config)
    
    return ModelConfigOut(
        id=model_config.id,
        model_name=model_config.model_name,
        stock_symbol=data_in.stock_symbol,
        input_size=model_config.input_size,
        num_lstm_layers=model_config.num_lstm_layers,
        lstm_size=model_config.lstm_size,
        dropout=model_config.dropout,
        description=model_config.description
    )