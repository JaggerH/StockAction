from fastapi import APIRouter, Depends
from ..dependencies import get_api_key
from utilities.tushare_utils import fetch_tushare_data, generic_transform_tushare_data
from utilities.tushare_models import *

router = APIRouter()

@router.post("/stock_list/", response_model=StockListResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def stock_list(request: StockListRequest):
    response_data = await fetch_tushare_data("stock_basic", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return StockListResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/a_stock_daily/", response_model=AShareDailyResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def a_stock_daily(request: AShareDailyRequest):
    response_data = await fetch_tushare_data("daily", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return AShareDailyResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/income/", response_model=IncomeResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def income(request: IncomeRequest):
    response_data = await fetch_tushare_data("income", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return IncomeResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/balance_sheet/", response_model=BalanceSheetResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def balance_sheet(request: BalanceSheetRequest):
    response_data = await fetch_tushare_data("balancesheet", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return BalanceSheetResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/cashflow/", response_model=CashflowResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def cashflow(request: CashflowRequest):
    response_data = await fetch_tushare_data("cashflow", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return CashflowResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/main_business/", response_model=MainBusinessResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def main_business(request: MainBusinessRequest):
    response_data = await fetch_tushare_data("fina_mainbz", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return MainBusinessResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/concept/", response_model=ConceptResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def concept(request: ConceptRequest):
    response_data = await fetch_tushare_data("concept", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return ConceptResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/limit_list/", response_model=LimitListResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def limit_list(request: LimitListRequest):
    response_data = await fetch_tushare_data("limit_list_d", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return LimitListResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/daily_basic/", response_model=DailyBasicResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def daily_basic(request: DailyBasicRequest):
    response_data = await fetch_tushare_data("daily_basic", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return DailyBasicResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/index_member/", response_model=IndexMemberResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def index_member(request: IndexMemberRequest):
    response_data = await fetch_tushare_data("index_member", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return IndexMemberResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/daily_info/", response_model=DailyInfoResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def daily_info(request: DailyInfoRequest):
    response_data = await fetch_tushare_data("daily_info", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return DailyInfoResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/ths_index/", response_model=ThsIndexResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def ths_index(request: ThsIndexRequest):
    response_data = await fetch_tushare_data("ths_index", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return ThsIndexResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/ths_daily/", response_model=ThsDailyResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def ths_daily(request: ThsDailyRequest):
    response_data = await fetch_tushare_data("ths_daily", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return ThsDailyResponse(code=response_data['code'], msg=response_data['msg'], data=data)

@router.post("/ths_member/", response_model=ThsMemberResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def ths_member(request: ThsMemberRequest):
    response_data = await fetch_tushare_data("ths_member", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return ThsMemberResponse(code=response_data['code'], msg=response_data['msg'], data=data)

