from app.main import get_session
from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.routes.data.Dto.inDataDto import AcquireDataIn
from app.routes.data.Dto.outDataDto import AcquireDataOut
from app.services.data import acquisition_service  # Placeholder

router = APIRouter()

@router.post("/acquire", response_model=AcquireDataOut, description="Fetches stock data from Alpha Vantage and persists it for training.")
def acquire_data(data_in: AcquireDataIn, session: Session = Depends(get_session)):
    result = acquisition_service.acquire_data(
        symbol=data_in.symbol,
        data_source=data_in.data_source, 
        outputsize=data_in.outputsize,
        session=session
    )
    return AcquireDataOut(
        symbol=result["symbol"],
        data_points=[{"date": dp.date, "adjusted_close": dp.adjusted_close} for dp in result["data_points"]],
        num_data_points=result["num_data_points"],
        date_range=result["date_range"]
    )