import os
from dotenv import load_dotenv
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

# how to get cosmos parameters
# create cosmos db on Microsoft Azure. website will give you a sample code zip, params are in config.
def set_env():
    if os.getenv("ENV") != "product":
        # 在开发环境中加载 .env 文件
        load_dotenv(override=True)

def create_stored_procedure(container):
    with open('./utilities/procedure/bulkInsert.js', 'r') as file:
        bulkInsert_definition = file.read()

    try:
        sproc = {
            'id': 'bulkInsert',
            'serverScript': bulkInsert_definition,
        }
        bulkInsert_sproc = container.scripts.create_stored_procedure(body=sproc)
        print("Stored procedure 'bulkInsert' created")
        return bulkInsert_sproc
    except exceptions.CosmosResourceExistsError:
        print("Stored procedure 'bulkInsert' already exists")

def init_container():
    set_env()
    ACCOUNT_HOST = os.getenv("ACCOUNT_HOST")
    ACCOUNT_KEY = os.getenv("ACCOUNT_KEY")
    COSMOS_DATABASE = os.getenv("COSMOS_DATABASE")
    COSMOS_CONTAINER = os.getenv("COSMOS_CONTAINER")

    client = cosmos_client.CosmosClient(ACCOUNT_HOST, {'masterKey': ACCOUNT_KEY})
    try:
        # setup database
        try:
            db = client.create_database(id=COSMOS_DATABASE)
        except exceptions.CosmosResourceExistsError:
            db = client.get_database_client(COSMOS_DATABASE)

        # setup container
        try:
            container = db.create_container(id=COSMOS_CONTAINER, partition_key=PartitionKey(path='/partitionKey'))
            create_stored_procedure(container)
            return container
        except exceptions.CosmosResourceExistsError:
            container = db.get_container_client(COSMOS_CONTAINER)
            return container
    except exceptions.CosmosHttpResponseError as e:
        print('azure cosmos has caught an error. {0}'.format(e.message))

def query_items(container, partitionKey):
    # Including the partition key value of partitionKey in the WHERE filter results in a more efficient query
    items = list(container.query_items(
        query="SELECT * FROM r WHERE r.partitionKey=@partitionKey",
        parameters=[
            { "name":"@partitionKey", "value": partitionKey }
        ]
    ))
    return items