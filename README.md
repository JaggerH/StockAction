# Running the Server
## Use Azure Function
I decide to use azure to hold my service, so this is the recommand method now.
I use Visual Studio Code, refer to the repo:
[fastapi-on-azure-functions](https://github.com/Azure-Samples/fastapi-on-azure-functions/) 
## Use docker
### STEP 1. start docker
```
docker-compose up
```
### STEP 2. run web server
To run the server, navigate to the chatgpt_api directory and run:
```
uvicorn app.main:app --reload --host=0.0.0.0 --port=8000
```
This command starts the Uvicorn server with live reloading.

# Build Tushare Models
后期考虑通过BeautifulSoup自动生成tushare_models.py
## 使用方式
复制utilities\inject_tushare_web_generate_model.js下的generateModelCode函数到Tushare页面的控制台
```
$table = $($('table')[0])
generateModelCode("BalanceSheetInfo", $table)
```
生成的结果手动复制到复制utilities\tushare_models.py

## 当前支持的接口
| 支持的接口 | operationID | 链接 |
| ------------- | ----------- | ------------- |
| 查询股票列表 | stock_list | [链接](https://tushare.pro/document/2?doc_id=25) |
| 查询A股日线行情 | a_stock_daily | [链接](https://tushare.pro/document/2?doc_id=27) |
| 获取上市公司利润表 | income | [链接](https://tushare.pro/document/2?doc_id=33) |
| 获取上市公司资产负债表 | balance_sheet | [链接](https://tushare.pro/document/2?doc_id=36) |
| 获取主营业务构成 | main_business | [链接](https://tushare.pro/document/2?doc_id=81) |