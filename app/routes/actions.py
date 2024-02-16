from fastapi import APIRouter, Depends, HTTPException
from ..models import ActionRequest, ActionResult
from ..dependencies import get_api_key
from utilities.tushare_utils import fetch_tushare_data, generic_transform_tushare_data
import httpx

router = APIRouter()

@router.post("/echo/", response_model=ActionResult, dependencies=[Depends(get_api_key)])
def echo_action(request: ActionRequest):
    # Simple action that echoes the received text
    return ActionResult(result=f"Echo: {request.text}")

@router.post("/reverse/", response_model=ActionResult)
def reverse_action(request: ActionRequest):
    reversed_text = request.text[::-1]
    return ActionResult(result=f"Reversed: {reversed_text}")

from ..models import StockInfo, QueryStockListRequest, QueryStockListResponse
@router.post("/query_stock_list/", response_model=QueryStockListResponse)
async def query_stock_list(request: QueryStockListRequest):
    response_data = await fetch_tushare_data("stock_basic", request.params, request.fields)

    stock_info_list = generic_transform_tushare_data(response_data, StockInfo)
    return QueryStockListResponse(code=response_data['code'], msg=response_data['msg'], data=stock_info_list)