import uvicorn
from fastapi import FastAPI
import script.core.services.crud_services


app = FastAPI()
app.include_router(script.core.services.crud_services.app_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
