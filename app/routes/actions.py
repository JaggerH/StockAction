from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_api_key
from utilities.tushare_utils import fetch_tushare_data, generic_transform_tushare_data
from ..models import *
from utilities.tushare_models import *
import httpx

router = APIRouter()

@router.post("/stock_list/", response_model=StockListResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def stock_list(request: StockListRequest):
    response_data = await fetch_tushare_data("stock_basic", request.params, request.fields)
    data = generic_transform_tushare_data(response_data, StockListFields)
    return StockListResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/a_stock_daily/", response_model_exclude_none=True, response_model=AShareDailyResponse)#, dependencies=[Depends(get_api_key)])
async def a_stock_daily(request: AShareDailyRequest):
    response_data = await fetch_tushare_data("daily", request.params, request.fields)
    data = generic_transform_tushare_data(response_data, AShareDailyFields)
    return AShareDailyResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/income/", response_model=IncomeResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def income(request: IncomeRequest):
    response_data = await fetch_tushare_data("income", request.params, request.fields)
    data = generic_transform_tushare_data(response_data, IncomeFields)
    return IncomeResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/balance_sheet/", response_model=BalanceSheetResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def balance_sheet(request: BalanceSheetRequest):
    response_data = await fetch_tushare_data("balancesheet", request.params, request.fields)
    data = generic_transform_tushare_data(response_data, BalanceSheetFields)
    return BalanceSheetResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/main_business/", response_model=MainBusinessResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def main_business(request: MainBusinessRequest):
    response_data = await fetch_tushare_data("fina_mainbz", request.params, request.fields)
    data = generic_transform_tushare_data(response_data, MainBusinessFields)
    return MainBusinessResponse(code=response_data['code'], msg=response_data['msg'], data=data)
