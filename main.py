import uvicorn

def start():
    uvicorn.run(
        "api.webapi:app",
        host="127.0.0.1",
        port=8070,
        reload=True
    )

if __name__ == "__main__":  
    start()
