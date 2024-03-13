# Running the Server
## Use Azure Function
I decide to use azure to hold my service, so this is the recommand method now.
I use Visual Studio Code, refer to the repo:
[fastapi-on-azure-functions](https://github.com/Azure-Samples/fastapi-on-azure-functions/) 
## Start Service
### Option 1. Use docker
```
docker-compose up
```
### Option 2. Use venv
set virtual environment
```
python3 -m venv .venv
./.venv/bin/active
pip install -r requirements.txt
```
set environment variables
```
# macOS
export LOGIN_API_KEY=YOUR_API_KEY
export TUSHARE_API_KEY=YOUR_API_KEY

# windows
$env:LOGIN_API_KEY='YOUR_API_KEY'
$env:TUSHARE_API_KEY='YOUR_API_KEY'
```
To run the server, navigate to the chatgpt_api directory and run:
```
uvicorn app.main:app --reload --host=0.0.0.0 --port=8000
```
This command starts the Uvicorn server with live reloading.

# Build Tushare Models
通过BeautifulSoup自动生成tushare_models.py
## 使用方式
### 步骤一
编辑.\utilities\tushare_api_list.csv
### 步骤二
```
python .\utilities\tushare_api_capture.py
```
生成的结果默认替换tushare_actions.py和tushare_models.py

### 当前支持的接口
| 支持的接口 | router | Model Name | 链接 |
| ------------- | ----------- | ------------- | ------------- |
| 股票列表 | stock_list | StockList | [链接](https://tushare.pro/document/2?doc_id=25) |
| A股日线行情 | a_stock_daily | AShareDaily | [链接](https://tushare.pro/document/2?doc_id=27) |
| 利润表 | income | Income | [链接](https://tushare.pro/document/2?doc_id=33) |
| 资产负债表 | balance_sheet | BalanceSheet | [链接](https://tushare.pro/document/2?doc_id=36) |
| 现金流量表 | cashflow | Cashflow | [链接](https://tushare.pro/document/2?doc_id=44) |
| 主营业务构成 | main_business | MainBusiness | [链接](https://tushare.pro/document/2?doc_id=81) |
| 概念股分类 | concept | Concept | [链接](https://tushare.pro/document/2?doc_id=125) |
| 涨跌停列表 | limit_list | LimitList | [链接](https://tushare.pro/document/2?doc_id=298) |
| 每日指标 | daily_basic | DailyBasic | [链接](https://tushare.pro/document/2?doc_id=32) |
| 申万行业成分构成 | index_member | IndexMember | [链接](https://tushare.pro/document/2?doc_id=182) |
| 市场交易统计 | daily_info | DailyInfo | [链接](https://tushare.pro/document/2?doc_id=215) |
| 同花顺概念和行业指数 | ths_index | ThsIndex | [链接](https://tushare.pro/document/2?doc_id=259) |
| 同花顺板块指数行情 | ths_daily | ThsDaily | [链接](https://tushare.pro/document/2?doc_id=260) |
| 同花顺概念板块成分 | ths_member | ThsMember | [链接](https://tushare.pro/document/2?doc_id=261) |

# Reference
[tr1s7an/CnInfoReports](https://github.com/tr1s7an/CnInfoReports)