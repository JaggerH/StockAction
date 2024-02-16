from fastapi import Header, HTTPException, status

async def get_api_key(api_key: str = Header(None)):
    expected_api_key = "your_expected_api_key"  # Replace with your actual API key
    if api_key != expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
