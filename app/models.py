from pydantic import BaseModel, Field
from typing import List, Optional, Generic, TypeVar
from pydantic.generics import GenericModel
from utilities.tushare_models import *
# Define a generic type variable
T = TypeVar('T')

# Define the generic response model
class TushareRequest(GenericModel, Generic[T]):
    params: Optional[T] = None
    fields: List[str]

# Define the generic response model
class TushareResponse(GenericModel, Generic[T]):
    code: int
    msg: Optional[str]
    data: Optional[T]

StockListRequest = TushareRequest[StockListParams]
StockListResponse = TushareResponse[List[StockListFields]]

AShareDailyRequest = TushareRequest[AShareDailyParams]
AShareDailyResponse = TushareResponse[List[AShareDailyFields]]

IncomeRequest = TushareRequest[IncomeParams]
IncomeResponse = TushareResponse[List[IncomeFields]]

BalanceSheetRequest = TushareRequest[BalanceSheetParams]
BalanceSheetResponse = TushareResponse[List[BalanceSheetFields]]

MainBusinessRequest = TushareRequest[MainBusinessParams]
MainBusinessResponse = TushareResponse[List[MainBusinessFields]]


