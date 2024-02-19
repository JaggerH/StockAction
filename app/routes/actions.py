from fastapi import APIRouter, Depends
from ..dependencies import get_api_key
from utilities.tushare_utils import fetch_tushare_data, generic_transform_tushare_data
from ..models import *
from utilities.tushare_models import *

router = APIRouter()

