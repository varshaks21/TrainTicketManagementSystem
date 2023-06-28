from fastapi import FastAPI, Request, APIRouter
# from script.core.handlers import train_management
import script.core.handlers.train_management
from script.constants.app_constants import Endpoint

app = FastAPI()
app_router = APIRouter()

@app_router.get(Endpoint.signup)
async def user_sign(request: Request):
    return await script.core.handlers.train_management.user_signup(request)

@app_router.get('/')
async def user(request: Request):
    return await script.core.handlers.train_management.login(request)

@app_router.get(Endpoint.create)
async def ticket_reservation(request: Request):
    return await script.core.handlers.train_management.ticket_reserve(request)

@app_router.get(Endpoint.update)
async def updated(request: Request):
    return await script.core.handlers.train_management.update_ticket(request)

@app_router.get(Endpoint.delete)
async def deleted(request: Request):
    return await script.core.handlers.train_management.delete_ticket(request)

@app_router.post(Endpoint.signup)
async def signup_post(request: Request):
    return await script.core.handlers.train_management.signup(request)

@app_router.post(Endpoint.login)
async def user_login(request: Request):
    return await script.core.handlers.train_management.login1(request)

@app_router.post(Endpoint.create)
async def ticketed_1(request: Request):
    return await script.core.handlers.train_management.ticket_reserved1(request)

@app_router.post(Endpoint.update)
async def updated_1(request: Request):
    return await script.core.handlers.train_management.update_ticket1(request)

@app_router.post(Endpoint.delete)
async def deleted_1(request: Request):
    return await script.core.handlers.train_management.delete_ticket1(request)
