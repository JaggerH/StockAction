import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

# 设置API密钥和数据库ID
api_key = os.getenv("NOTION_API_KEY")
database_id = os.getenv("NOTION_DATABASE_ID")

# 设置请求头
headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"  # 替换为你使用的Notion API版本
}

def build_records(properties):
    return {
        "parent": {"database_id": database_id},
        "properties": properties
    }

def create_records(properties):
    try:
        records = build_records(properties)
        response = requests.post('https://api.notion.com/v1/pages', headers=headers, json=records)

        # 检查响应状态码
        if response.status_code == 200:
            print("Data added successfully!")
        else:
            print("Response:", response.json())
            raise("Failed to add data. Status code:", response.status_code)
    except Exception as e:
        print("Response:", e)

def retrive_database():
    try:
        response = requests.post(f'https://api.notion.com/v1/databases/{database_id}/query', headers=headers)
        data = response.json()
        # 检查响应状态码
        if response.status_code != 200:
            print("Response:", response.json())
            raise("Failed to fetch database entries. Status code:", response.status_code)

        return data
    except Exception as e:
        print("Response:", e)

def update_database(page_id, properties):
    try:
        # 发送PATCH请求以更新条目
        response = requests.patch(f'https://api.notion.com/v1/pages/{page_id}', headers=headers, json=properties)

        # 检查响应状态码
        if response.status_code != 200:
            print("Response:", response.json())
            raise("Failed to fetch database entries. Status code:", response.status_code)

        return True
    except Exception as e:
        print("Response:", e)
        return False
    
def is_expired(time_str):
    time_format = "%Y-%m-%d"  # 时间字符串的格式
    time = datetime.strptime(time_str, time_format)  # 将时间字符串转换为datetime对象
    now = datetime.now()  # 当前时间
    thirty_days_ago = now - timedelta(days=30)  # 30天前的时间
    return time <= thirty_days_ago  # 如果时间早于等于30天前的时间，则返回True，否则返回False
