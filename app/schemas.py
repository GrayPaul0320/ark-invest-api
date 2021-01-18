import datetime
from typing import List, Optional
from pydantic import BaseModel


class FundList(BaseModel):
    symbol: str
    name: str
    description: str

    class Config:
        orm_mode = True


class FundProfile(BaseModel):
    profile: List[FundList] = []

    class Config:
        orm_mode = True


class HoldingList(BaseModel):
    company: str
    ticker: Optional[str]
    cusip: str
    shares: int
    market_value: float
    weight: float
    weight_rank: int

    class Config:
        orm_mode = True


class FundHolding(BaseModel):
    symbol: str
    date: datetime.date
    holdings: List[HoldingList] = []

    class Config:
        orm_mode = True


class TradeList(BaseModel):
    date: datetime.date
    direction: str
    ticker: Optional[str]
    company: str
    cusip: str
    shares: int
    etf_percent: float

    class Config:
        orm_mode = True


class FundTrades(BaseModel):
    symbol: str
    date_from: datetime.date
    date_to: datetime.date
    trades: List[TradeList] = []

    class Config:
        orm_mode = True


class StockProfile(BaseModel):
    ticker: str
    name: Optional[str]
    country: Optional[str]
    industry: Optional[str]
    sector: Optional[str]
    fullTimeEmployees: Optional[int]
    summary: Optional[str]
    website: Optional[str]
    market: Optional[str]
    exchange: Optional[str]
    currency: Optional[str]
    marketCap: Optional[float]
    sharesOutstanding: Optional[int]

    class Config:
        orm_mode = True
