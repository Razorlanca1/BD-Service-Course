import uvicorn

if __name__ == "__main__":
    uvicorn.run("practical_tasks:practical_router", host="127.0.0.9", port=8008, log_level="info", reload=True)