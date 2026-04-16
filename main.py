import uvicorn

# Funcion que inicia el servidor con uvicorn
def start():
    uvicorn.run(
        "api.ownerWebApi:app",
        host="127.0.0.1",
        port=8070,
        reload=True
    )

if __name__ == "__main__":  
    start()
