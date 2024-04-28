import os, sys
from utils.str_helper import match_security_in_text
from utils.notion_helper import create_records, retrive_database, is_expired
from dotenv import load_dotenv
load_dotenv()
import tushare as ts
from datetime import datetime, timedelta
import json
import pandas as pd

tushare_api_key = os.getenv("TUSHARE_API_KEY")
pro = ts.pro_api(tushare_api_key)

def get_securities():
    return pro.stock_basic(**{ "ts_code": "", "name": "", "exchange": "", "market": "", }, fields=[ "ts_code", "symbol", "name", "area", "industry", "cnspell", "market", "list_date", "act_name", "act_ent_type" ])

def get_price(trade_date):
    trade_date = str(trade_date).replace("-", "")
    return pro.daily(**{ "trade_date": trade_date }, fields=[ "ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount" ])

def get_trade_days(date):
    # 获得两年前的日期
    start_date = str(date - timedelta(days=365*2)).replace("-", "")
    end_date = str(date).replace("-", "")
    return pro.trade_cal(**{ "start_date": start_date, "end_date": end_date, "is_open": 1, }, fields=[ "exchange", "cal_date", "is_open", "pretrade_date" ])

def main():
    if len(sys.argv) > 1:
        input_arg = sys.argv[1]
    else:
        print("Usage: python observe_security.py <input_file>")
        return

    if not os.path.exists(input_arg):
        print("Error: File not found.")
        return

    # ---------------------
    # df 股票基本信息
    # date 今日日期
    # latest_trade_date 最近交易日期
    # price 最近交易日期股票价格
    # ---------------------
    security = get_securities()
    date = datetime.now().date()
    latest_trade_date = get_trade_days(date).loc[0, 'cal_date']
    price = get_price(latest_trade_date)

    # ---------------------
    # 增加记录的逻辑
    # ---------------------
    # txt_path = os.path.splitext(input_arg)[0] + '.txt'
    # with open(txt_path, "r", encoding="utf-8") as f:
    #     text = f.read()
    #     securities = match_security_in_text(text)
    #     filtered_df = security[security['symbol'].isin(securities)]

    # codes = filtered_df['ts_code'].tolist()
    # # 询问用户，date中的日期是否可以用作后续的参数
    # # if input(f"{latest_trade_date}, Is the date correct? (y/n) ") != "y":
    # #     latest_trade_date = datetime.strptime(input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d").date()
    # filter_price = price[price['ts_code'].isin(codes)]

    # # combine filtered_df and price by ts_code
    # res_df = filtered_df.merge(filter_price, on='ts_code')
    # # convert latest_trade_date str to datetime from format YYYYMMDD
    # res_df['time'] = str(datetime.strptime(latest_trade_date, "%Y%m%d").date())
    # res_df = res_df[['time', 'symbol', 'name', 'close']]

    # for index, row in res_df.iterrows():
    #     properties = {
    #         "推送时间": {"title": [{"text": {"content": row['time']}}]},
    #         "股票代码": {"rich_text": [{"text": {"content": row['symbol']}}]},
    #         "股票名称": {"rich_text": [{"text": {"content": row['name']}}]},
    #         "届时股价": {"number": row['close']} 
    #     }
    #     create_records(properties)

    # ---------------------
    # 更新记录的逻辑
    # ---------------------
    data = retrive_database()
    dates = []
    codes = []
    items = []
    for item in data['results']:
        page_id = item['id']
        time = item['properties']['推送时间']['title'][0]['text']['content']
        symbol = item['properties']['股票代码']['rich_text'][0]['text']['content']

        dates.append(time)
        codes.append(symbol)

        Type_value = "Expired" if is_expired(time) else "Tracking"

    min_date = min(dates)
    ts_codes = security[security['symbol'].isin(codes)].iloc['ts_code']

    part_price = pro.daily(**{
        "ts_code": ts_codes.value,
        "start_date": min_date.replace("-", ""),
        "end_date": latest_trade_date
    }, fields=[ "ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount" ])

    current_price = price[price['ts_code'].isin(ts_codes)]
    print(part_price.head())
    print(current_price.head())
        # print(time, symbol, Type_value, current_price)
        # break
        # properties = {
        #     "properties": {
        #         "Type": {"select": {"name": Type_value}}  # 选择Select属性并设置相应的值
        #         # 根据你的数据库结构添加更多属性
        #     }
        # }
        # update_database(page_id, properties)
if __name__ == "__main__":
    main()