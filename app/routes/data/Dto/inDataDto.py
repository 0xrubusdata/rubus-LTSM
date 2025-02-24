from pydantic import BaseModel
from typing import Optional, Literal

class AcquireDataIn(BaseModel):
    symbol: str  # e.g., "IBM" for stocks, "BTCUSD" for crypto
    data_source: Literal[
        "timeseries", "fundamentaldata", "techindicators", "cryptocurrencies",
        "foreignexchange", "commodities", "econindicators", "options", "alphaintelligence"
    ]  # Supported Alpha Vantage APIs
    outputsize: Optional[str] = "full"  # Relevant for timeseries, crypto, etc.