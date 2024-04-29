"""
这个脚本是用于观测和更新Notion中Database中的股票价格

有很多公众号或者视频号推荐股票
通过持续跟踪观察他们推荐的股票在一个月内的走势

脚本每天运行
1. 从Database读取数据
2. 如果推送超过一个月则判定为失效
3. 更新未失效的股票价格
"""
import os
from notion_client import Client
from utilities.notion import update

import pandas as pd
from datetime import datetime, timedelta
from utilities.notion import retrieve_database
from utilities.tushare_utils import getLatestTradeData, getSecurityInfo, getDailyPrice

def prepare_data(df):
    start_date = df['推送时间'].min().replace("-", "")
    columns = df.columns
    index = df.index
    latest_trade_date = getLatestTradeData()
    info = getSecurityInfo()

    filter_info = info[info['symbol'].isin(df['股票代码'])]
    filter_info = filter_info[['symbol', 'ts_code']]

    price = getDailyPrice(ts_code=",".join(filter_info['ts_code'].values), start_date=start_date, end_date=latest_trade_date)

    return df, price, filter_info, columns, index

def update_Type(time_str):
    time_format = "%Y-%m-%d"  # 时间字符串的格式
    time = datetime.strptime(time_str, time_format)  # 将时间字符串转换为datetime对象
    now = datetime.now()  # 当前时间
    thirty_days_ago = now - timedelta(days=30)  # 30天前的时间
    return "Tracking" if time >= thirty_days_ago else "Expired" # 如果时间早于等于30天前的时间，则返回True，否则返回False

def process_data(_df, price, info, columns, index):
    df = _df.copy()

    # info包含symbol, ts_code
    # 通过merge为df增加ts_code，为后续的相关价格修改做准备
    df['symbol'] = df['股票代码']
    df = pd.merge(df, info, on='symbol')

    # 更新 当前价格
    latest_price = price[price['trade_date'] == price['trade_date'].max()]
    latest_price = latest_price[['ts_code', 'close']]
    df = pd.merge(df, latest_price, on='ts_code')
    df['当前价格'] = df['close']

    # 更新 Max Price
    for idx, row in df.iterrows():
        interval_price = price[price['ts_code'] == row['ts_code']]
        interval_price = interval_price[interval_price['trade_date'] >= row['推送时间'].replace("-", "")]
        df.loc[idx, 'Max Price'] = interval_price['high'].max()

    # 更新 Type
    df['Type'] = df['推送时间'].apply(update_Type)

    # 更新 Pct Change
    df['Pct Change'] = (df['当前价格'] - df['届时股价']) / df['届时股价']
    df['Pct Change'] = df['Pct Change'].round(4)

    # 解决由于merge导致的缺乏index的问题
    df.index = index
    # 只保留需要的列
    df = df[columns]
    print(df)
    return df

def update_tracking_security(database_id):
    client = Client(auth=os.environ["NOTION_API_KEY"])
    # database_id = os.environ["NOTION_DATABASE_ID"]
    df = retrieve_database(client.databases.query, database_id=database_id, filter={"property": "Type", "select": {"equals": "Tracking"}})

    df, price, info, columns, index = prepare_data(df)
    df = process_data(df, price, info, columns, index)

    update(df, database_id, client)