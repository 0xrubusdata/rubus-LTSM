from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.commodities import Commodities
from alpha_vantage.econindicators import EconomicIndicators
# Note: Options and AlphaIntelligence may not be directly available in the library; adjust as needed
from app.config.settings import CONFIG

class AlphaVantageFactory:
    @staticmethod
    def get_service(data_source: str):
        key = CONFIG["alpha_vantage"]["key"]
        services = {
            "timeseries": lambda: TimeSeries(key=key),
            "fundamentaldata": lambda: FundamentalData(key=key),
            "techindicators": lambda: TechIndicators(key=key),
            "cryptocurrencies": lambda: CryptoCurrencies(key=key),
            "foreignexchange": lambda: ForeignExchange(key=key),
            "commodities": lambda: Commodities(key=key),
            "econindicators": lambda: EconomicIndicators(key=key),
            # Placeholder for unsupported APIs; extend when available
            "options": lambda: None,  # Not directly supported; custom implementation needed
            "alphaintelligence": lambda: None  # Not directly supported; custom implementation needed
        }
        service = services.get(data_source)
        if service is None or service() is None:
            raise ValueError(f"Unsupported or unimplemented data source: {data_source}")
        return service()

alpha_vantage_factory = AlphaVantageFactory()