import pandas as pd
from utilities.set_env import set_env
from notion_client import Client
from notion_df.values import PageProperties, PageProperty
from typing import List, Dict, Callable, Any
from notion_client.helpers import iterate_paginated_api
from notion_df.configs import DatabaseSchema
import warnings

def load_df_from_queries(
    database_query_results: List[Dict],
):
    properties = PageProperties.from_raw(database_query_results)
    df = properties.to_frame()

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        df.notion_urls = pd.Series([ele["url"] for ele in database_query_results])
        df.notion_ids = pd.Series([ele["id"] for ele in database_query_results])
        df.notion_query_results = database_query_results

    return df

def load_database_schema(database_id, client):
    return DatabaseSchema.from_raw(
        client.databases.retrieve(database_id=database_id)["properties"]
    )

def retrieve_database(function: Callable[..., Any], **kwargs: Any) -> pd.DataFrame:
    """
    Params is the same with notion_client.helpers.async_iterate_paginated_api
    return: pd.DataFrame
    example:
    retrieve_database(client.databases.query, database_id=database_id, filter={"property": "Type", "select": {"equals": "Tracking"}})

    """
    downloaded_rows = []
    for block in iterate_paginated_api(function, **kwargs):
        downloaded_rows.append(block)

    index = [ item['id'] for item in downloaded_rows ]
    df = load_df_from_queries(downloaded_rows)
    df.index = index

    return df

def update(
    df: pd.DataFrame,
    database_id: str,
    client,
    schema: DatabaseSchema = None,
):
    if schema is None:
        if hasattr(df, "schema"):
            schema = df.schema
        else:
            schema = load_database_schema(database_id, client)

    assert schema is not None

    all_response = []

    for index, row in df.iterrows():
        try:
            properties = PageProperty.from_series(row, schema).query_dict()
            response = client.pages.update(index, properties=properties)
            all_response.append(response)
        except Exception as e:
            raise e
            continue
    return all_response