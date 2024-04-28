import os
import httpx
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional, Type, List
import tushare as ts
from datetime import datetime

token = os.getenv('TUSHARE_API_KEY')
pro = ts.pro_api(token)

async def fetch_tushare_data(api_name: str, params: Optional[dict], fields: list) -> dict:
    url = "http://api.tushare.pro"
    token = os.getenv('TUSHARE_API_KEY')
    json_data = {
        "api_name": api_name,
        "token": token,
        "params": params.dict(exclude_none=True) if params else {},
        "fields": ",".join(fields)
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=json_data)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error in TuShare API call")
        
        return response.json()

def generic_transform_tushare_data(response_data: dict) -> List[BaseModel]:
    if not response_data.get('data') or not response_data['data'].get('items'):
        return []

    fields = response_data['data']['fields']
    items = response_data['data']['items']
    return [dict(zip(fields, item)) for item in items]

def getLatestTradeData(specific_date=None) -> str:
    """
        如果今天不是交易日期，将返回最近交易日
    """
    today_str = specific_date if specific_date is not None else datetime.now().strftime("%Y%m%d")
    df = pro.trade_cal(**{ "exchange": "SSE", "cal_date": today_str }, fields=[ "exchange", "cal_date", "is_open", "pretrade_date" ])
    row = df.loc[0]
    return row['pretrade_date'] if row['is_open'] == 0 else row['cal_date']

def getSecurityInfo(**kwargs):
    """
    获取股票基本信息
    """
    return pro.stock_basic(**kwargs, fields=[ "ts_code", "symbol", "name", "area", "industry", "cnspell", "market", "list_date", "act_name", "act_ent_type" ])

def getDailyPrice(**kwargs):
    """
    获取日线收盘价格
    """
    return pro.daily(**kwargs, fields=[ "ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount" ])