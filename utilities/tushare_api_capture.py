import requests
from bs4 import BeautifulSoup
import csv
import os
import re

# Constants
TUSHARE_MODELS_PATH = r'./utilities/tushare_models.py'
TUSHARE_ACTIONS_PATH = r'./app/routes/tushare_actions.py'
INTERFACE_LIST_PATH = r'./utilities/tushare_api_list.csv'

def read_interface_list(path):
    interface_list = []
    with open(path, 'rb') as file:
        csv_reader = csv.DictReader(line.decode('utf-8', 'ignore') for line in file)
        for row in csv_reader:
            interface = {
                'link_name': row['router'],
                'model_name': row['Model Name'],
                'url': row['link']
            }
            interface_list.append(interface)
    return interface_list

def scrape_web_page(url):
    """
    Scrapes a web page and returns its HTML content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops: Something Else", err)
    return None

def match_api_name(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Search for the "接口：" text and extract the following text for the API name
    api_name_element = soup.find(string=lambda text: text and "接口：" in text)
    if api_name_element:
        # The API name is assumed to follow "接口：" and be on the same line
        pattern = r'[A-Za-z_]'
        # Find all occurrences of the pattern
        letters = re.findall(pattern, api_name_element)
        api_name = ''.join(letters)
    else:
        api_name = None

    return api_name

def parse_table_data(html_content):
    """
    Parses table data from HTML content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    all_tables_data = []

    for table in tables:
        headers = []
        table_data = []
        rows = table.find_all('tr')
        
        for header in rows[0].find_all('th'):
            headers.append(header.text.strip())

        for row in rows[1:]:
            cells = row.find_all('td')
            row_data = {headers[i]: cells[i].text.strip() for i in range(len(cells))}
            table_data.append(row_data)

        all_tables_data.append(table_data)

    return all_tables_data

def generate_model_code(model_name, table_data):
    """
    Generates Python model code from table data.
    """
    model_code = f'class {model_name}(BaseModel):\n'
    for row in table_data:
        field_name = row.get('名称', '').strip()
        field_type = row.get('类型', '').strip()
        field_description = row.get('描述', '').strip()

        if field_name and field_type:
            model_field = f'    {field_name}: Optional[{field_type}] = None  # {field_description}\n'
            model_code += model_field
    
    if model_name.endswith('Params'):
        class_name = model_name.split('Params')[0]
        model_code += f'\n{class_name}Request = TushareRequest[{model_name}]\n'

    if model_name.endswith('Fields'):
        class_name = model_name.split('Fields')[0]
        model_code += f'\n{class_name}Response = TushareResponse[List[{model_name}]]\n'

    return model_code

def write_code_to_file(code, file_name=TUSHARE_MODELS_PATH):
    """
    Writes the generated model code to a file.
    """
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(code + '\n')

def remove_file(file_path):
    if os.path.exists(file_path):
        try:
            # 删除文件
            os.remove(file_path)  # 或者使用 os.unlink(file_path)
            print(f"{file_path}存在，删除文件")
        except OSError as e:
            print(f"文件删除失败：{e}")

def preprocess_tushare_models():
    remove_file(TUSHARE_MODELS_PATH)
    code = """from pydantic import BaseModel, Field
from typing import List, Optional, Generic, TypeVar
from pydantic.generics import GenericModel

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
    """
    write_code_to_file(code, TUSHARE_MODELS_PATH)

def preprocess_tushare_actions():
    remove_file(TUSHARE_ACTIONS_PATH)
    code = """from fastapi import APIRouter, Depends
from ..dependencies import get_api_key
from utilities.tushare_utils import fetch_tushare_data, generic_transform_tushare_data
from utilities.tushare_models import *

router = APIRouter()
"""
    write_code_to_file(code, TUSHARE_ACTIONS_PATH)

def writeRoute(router, model_name, api_name):
    code = f"""@router.post("/{router}/", response_model={model_name}Response, response_model_exclude_none=True, dependencies=[Depends(get_api_key)])
async def {router}(request: {model_name}Request):
    response_data = await fetch_tushare_data("{api_name}", request.params, request.fields)
    data = generic_transform_tushare_data(response_data)
    return {model_name}Response(code=response_data['code'], msg=response_data['msg'], data=data)
"""
    write_code_to_file(code, TUSHARE_ACTIONS_PATH)

def main():
    """
    Main script logic.
    """
    preprocess_tushare_models()
    preprocess_tushare_actions()

    interface_list = read_interface_list(INTERFACE_LIST_PATH)
    for interface in interface_list:
        html_content = scrape_web_page(interface['url'])
        if html_content:
            interface['api_name'] = match_api_name(html_content)
            table_data = parse_table_data(html_content)
            model_code = generate_model_code(interface['model_name'] + "Params", table_data[0])
            write_code_to_file(model_code, TUSHARE_MODELS_PATH)

            if interface['link_name'] == 'daily_info': # daily_info的Fields在第三个表格
                model_code = generate_model_code(interface['model_name'] + "Fields", table_data[2])
                write_code_to_file(model_code, TUSHARE_MODELS_PATH)
            else:
                model_code = generate_model_code(interface['model_name'] + "Fields", table_data[1])
                write_code_to_file(model_code, TUSHARE_MODELS_PATH)
            writeRoute(interface['link_name'], interface['model_name'], interface['api_name'])

if __name__ == '__main__':
    main()
