from fastapi import APIRouter, Depends
from ..dependencies import get_api_key
from utilities.tushare_utils import fetch_tushare_data, generic_transform_tushare_data
from ..models import *
from utilities.tushare_models import *
import logging
from sys import stdout
from utilities.CnInfoReport import CnInfoReports

router = APIRouter()

@router.post("/annoucement/", response_model=AnnouncementResponse, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def annoucement(request: AnnouncementRequest):
    filter = request.dict(exclude_none=True) if request else {}
    instance = CnInfoReports(skip_download_stock_json=True)

    annoucements = instance.query_announcements_info(filter)
    for ann in annoucements:
        ann['adjunctUrl'] = 'http://static.cninfo.com.cn/' + ann['adjunctUrl']
    return { "data": annoucements }
