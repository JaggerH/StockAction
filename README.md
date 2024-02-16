Running the Server

## STEP 1. start docker
```
docker-compose up
```
## STEP 2. run web server
To run the server, navigate to the chatgpt_api directory and run:
```
uvicorn app.main:app --reload --host=0.0.0.0 --port=8000
```
This command starts the Uvicorn server with live reloading.