from sqlmodel import Session, select
from app.models import Stock, DataPoint
from app.config.settings import CONFIG
from factory.alpha_vantage_factory import alpha_vantage_factory
from .normalizationService import normalize_data
from .datasetprepService import prepare_dataset

class AcquisitionService:
    @staticmethod
    def acquire_data(symbol: str, data_source: str, outputsize: str, session: Session):
        # Check or create stock (assuming symbol is relevant across data sources)
        stock = session.exec(select(Stock).where(Stock.symbol == symbol)).first()
        if not stock:
            stock = Stock(symbol=symbol)
            session.add(stock)
            session.commit()
            session.refresh(stock)

        # Get the appropriate Alpha Vantage service
        service = alpha_vantage_factory.get_service(data_source)

        # Fetch data based on source (focus on time-series-like data for LSTM)
        if data_source == "timeseries":
            data, _ = service.get_daily_adjusted(symbol, outputsize=outputsize)
            key_value = CONFIG["alpha_vantage"]["key_adjusted_close"]
        elif data_source == "cryptocurrencies":
            data, _ = service.get_daily(symbol, market="USD", outputsize=outputsize)
            key_value = "4b. close (USD)"  # Adjust based on Alpha Vantage response
        elif data_source == "foreignexchange":
            data, _ = service.get_daily(from_symbol=symbol[:3], to_symbol=symbol[3:], outputsize=outputsize)
            key_value = "4. close"
        else:
            # Placeholder for non-time-series data; extend as needed
            raise ValueError(f"Data source '{data_source}' not yet supported for time-series prediction")

        # Extract and reverse data
        data_date = [date for date in data.keys()]
        data_date.reverse()
        data_close_price = [float(data[date][key_value]) for date in data.keys()]
        data_close_price.reverse()

        # Persist raw data as DataPoints
        data_points = []
        for date_str, price in zip(data_date, data_close_price):
            dp = DataPoint(stock_id=stock.id, date=date_str, adjusted_close=price)
            session.add(dp)
            data_points.append(dp)
        session.commit()

        # Normalize and prepare dataset
        norm_result = normalize_data(data_points, session)
        dataset_result = prepare_dataset(
            stock_id=stock.id,
            normalized_data=norm_result["normalized_values"],
            window_size=CONFIG["data"]["window_size"],
            train_split_size=CONFIG["data"]["train_split_size"],
            scaler=norm_result["scaler"],
            session=session
        )

        num_data_points = len(data_date)
        date_range = f"from {data_date[0]} to {data_date[-1]}"
        return {
            "symbol": symbol,
            "data_points": data_points,
            "num_data_points": num_data_points,
            "date_range": date_range,
            "dataset_id": dataset_result["dataset_id"]
        }

acquisition_service = AcquisitionService()