from pydantic import BaseModel, Field
from typing import List, Optional

class ActionRequest(BaseModel):
    text: str

class ActionResult(BaseModel):
    result: str

class StockInfo(BaseModel):
    ts_code: str
    symbol: str
    name: str
    area: str
    industry: str
    fullname: Optional[str]
    enname: Optional[str]
    cnspell: Optional[str]
    market: str
    exchange: Optional[str]
    curr_type: Optional[str]
    list_status: Optional[str]
    list_date: str
    delist_date: Optional[str]
    is_hs: Optional[str]
    act_name: Optional[str]
    act_ent_type: Optional[str]

class QueryStockListParam(BaseModel):
    ts_code: Optional[str] = None
    name: Optional[str] = None
    market: Optional[str] = None
    list_status: Optional[str] = None
    exchange: Optional[str] = None
    is_hs: Optional[str] = None

class QueryStockListRequest(BaseModel):
    params: Optional[QueryStockListParam] = None
    fields: List[str]

class QueryStockListResponse(BaseModel):
    code: int
    msg: Optional[str]
    data: Optional[List[StockInfo]] = None