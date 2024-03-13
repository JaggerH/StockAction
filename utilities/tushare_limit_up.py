import os
import tushare as ts
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Mapping English column names to Chinese
columns_mapping = {
    # 'trade_date': '交易日期',
    'ts_code': '股票代码',
    'name': '股票名称',
    'industry': '所属行业',
    'close': '收盘价',
    'pct_chg': '涨跌幅',
    'amount': '成交额(亿)',
    'circ_mv': '流通市值(亿)',
    'total_mv': '总市值(亿)',
    'pb': 'PB',
    'pe': 'PE',
    'turnover_rate': '换手率',
    'turnover_rate_f': '流通股换手率',
    'limit_amount': '板上成交金额(亿)',
    'fd_amount': '封单金额(亿)',
    'first_time': '首次封板时间',
    'last_time': '最后封板时间',
    'open_times': '炸板次数',
    'up_stat': '涨停统计',
    'limit_times': '连板数',
}

# 获取交易日历
def getLatestTradeData(pro, today_str):
    """
        如果今天不是交易日期，将返回最近交易日
    """
    df = pro.trade_cal(**{ "exchange": "SSE", "cal_date": today_str }, fields=[ "exchange", "cal_date", "is_open", "pretrade_date" ])
    row = df.loc[0]
    return row['pretrade_date'] if row['is_open'] == 0 else row['cal_date']

# 涨停数据
def getLimitUpData(pro, cal_date):
    limit_up_df = pro.limit_list_d(**{ "trade_date": cal_date, "limit_type": "U", }, fields=[ "trade_date", "ts_code", "limit_amount", "fd_amount", "first_time", "last_time", "open_times", "up_stat", "limit_times", "limit" ])
    daily_df = pro.daily(**{"trade_date": cal_date}, fields=[ "ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount" ])
    tenpct_df = daily_df[daily_df['pct_chg'] >= 10]

    stock_basic_df = pro.stock_basic(**{"list_status": 'L'}, fields=['ts_code','name','industry'])
    daily_basic_df = pro.daily_basic(**{"trade_date": cal_date}, fields=['ts_code','trade_date','circ_mv','total_mv','turnover_rate','turnover_rate_f','pe','pb'])

    # 合并tenpct_df和limit_up_df
    union_tscode = pd.concat([tenpct_df['ts_code'], limit_up_df['ts_code']]).drop_duplicates()
    union_tscode_df = daily_df[daily_df['ts_code'].isin(union_tscode)]
    merged_df = pd.merge(union_tscode_df, stock_basic_df, on=['ts_code'], how='left')
    merged_df = pd.merge(merged_df, daily_basic_df, on=['ts_code'], how='left')
    merged_df = pd.merge(merged_df, limit_up_df, on=['ts_code'], how='outer')

    return merged_df

def prepare_df(df):
    # Order the DataFrame by 'limit_times' in descending order
    limit_up_df_copy = df.sort_values(by='limit_times', ascending=False)
    # 预处理单位
    limit_up_df_copy['amount'] = limit_up_df_copy['amount'] * 1000 # 成交额 原单位应是千分位
    limit_up_df_copy['circ_mv'] = limit_up_df_copy['circ_mv'] * 10000 # 流值 原单位应是万
    limit_up_df_copy['total_mv'] = limit_up_df_copy['total_mv'] * 10000 # 总值 原单位应是万

    # 将金额单位全部换成亿
    limit_up_df_copy['amount'] = round(limit_up_df_copy['amount'] / 10000 / 10000, 2)
    limit_up_df_copy['limit_amount'] = round(limit_up_df_copy['limit_amount'] / 10000 / 10000, 2)
    limit_up_df_copy['circ_mv'] = round(limit_up_df_copy['circ_mv'] / 10000 / 10000, 2)
    limit_up_df_copy['total_mv'] = round(limit_up_df_copy['total_mv'] / 10000 / 10000, 2)
    limit_up_df_copy['fd_amount'] = round(limit_up_df_copy['fd_amount'] / 10000 / 10000, 2)

    columns_sequence = columns_mapping.keys()
    limit_up_df_copy = limit_up_df_copy.reindex(columns=columns_sequence)
    # Rename the columns using the mapping
    return limit_up_df_copy.rename(columns=columns_mapping)

def build_xlsx(df, cal_date):
    from openpyxl import Workbook
    from openpyxl.utils.dataframe import dataframe_to_rows
    from openpyxl.styles import numbers

    # Create a new Excel file with formatted values
    wb = Workbook()
    ws = wb.active

    for r in dataframe_to_rows(df, index=False, header=True):
        ws.append(r)

    ws.freeze_panes = 'A2'
    # Save the workbook
    excel_file_path = './涨停分析-%s.xlsx' % cal_date
    wb.save(excel_file_path)
    print("已写入路径：" + excel_file_path)

def generate_limit_up(specific_date=None):
    if os.getenv("ENV") != "product":
        # 在开发环境中加载 .env 文件
        load_dotenv(override=True)

    # 初始化pro接口
    token = os.getenv('TUSHARE_API_KEY')
    pro = ts.pro_api(token)

    # 如果有指定日期，使用指定日期，否则使用最近的交易日
    if specific_date:
        cal_date = specific_date
    else:
        # Generate today's date in "yyyymmdd" format
        today_str = datetime.now().strftime("%Y%m%d")
        cal_date = getLatestTradeData(pro, today_str)

    df = getLimitUpData(pro, cal_date)
    df = prepare_df(df)
    build_xlsx(df, cal_date)