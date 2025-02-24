from sqlmodel import SQLModel, Field
from typing import Optional

class Config(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    key: str = Field(max_length=50, unique=True, index=True)  # e.g., "alpha_vantage_key", "xticks_interval"
    value: str = Field(max_length=255)                        # Stored as string, parsed as needed
    description: Optional[str] = Field(default=None, max_length=255)