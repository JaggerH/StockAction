import os
import httpx
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional, Type, List

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

def generic_transform_tushare_data(response_data: dict, model: Type[BaseModel]) -> List[BaseModel]:
    if not response_data.get('data') or not response_data['data'].get('items'):
        return []

    fields = response_data['data']['fields']
    items = response_data['data']['items']
    return [model(**dict(zip(fields, item))) for item in items]