from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI, Request
import logging

from starlette.responses import RedirectResponse

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
file_handler = logging.FileHandler("login.log")
formatter = logging.Formatter('%(name)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


app = FastAPI()


# Connect to MongoDB
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
db = client.interns_b2_23
collection = db.varsha


class user(BaseModel):
    username: str
    password: str
    email: str

class Ticket(BaseModel):
    ticket_id: int
    date: str
    origin: str
    destination: str

@app.post("/user_signup")
async def user_signup(request: Request):
    data = await request.form()
    logger.debug('signup ')
    var = user(
        username=data["username"],
        password=data["password"],
        email=data["email"]
    )
    collection.insert_one(var.dict())
    return {"message": "Sign up successful"}


@app.post("/user_login")
async def user_login(request: Request):
    data = await request.form()
    username = data["username"]
    password = data["password"]
    var = collection.find_one({"username": username, "password": password})
    if var:
        logger.debug('login successful')
        return RedirectResponse(url="http://localhost:63342/pythonProject15/"
                                    "ticket_reservation.html?"
                                    "_ijt=i4h3rad90h7df7m9lfp86chr2q&_ij_reload=RELOAD_ON_SAVE", status_code=302)
        # return {"message": "login  Successfully"}
    else:
        logger.debug('not successful')
        return {"error": "Login failed, username or password is wrong!!"}


@app.post("/ticket_reserve")
async def ticket_reserve(request: Request):
    data = await request.form()
    ticket_id = data["ticket_id"]
    origin = data["origin"]
    destination = data["destination"]
    date = data["date"]
    var = collection.find_one({"ticket_id": ticket_id})
    if var:
        logger.debug('Ticket already Exist')
        return {"message": "Not possible"}
    else:
        var_1 = collection.insert_one({"ticket_id": ticket_id, "origin": origin, "destination": destination, "date": date})
        if var_1:
            logger.debug('Ticket Created successful')
            return {"message": "Successfully"}
        else:
            logger.debug('Ticket not created successful')
            return {"error": "Not successful"}


@app.post("/update_ticket")
async def update_ticket(request: Request):
    data = await request.form()
    date = data["date"]
    update_date = data["update_date"]
    user = collection.update_one({"date": date},
                                 {"$set": {"update_date": update_date}})
    if user.modified_count > 0:
        logging.info("Date updated Successfully")
        return {"successful"}
    else:
        logging.info("Update failed")
        return {"message": "date not updated"}

@app.post("/delete_ticket")
async def delete_ticket(request: Request):
    data = await request.form()
    ticket_id = data["ticket_id"]
    delete_ticket = collection.find_one({"ticket_id": ticket_id})
    if delete_ticket:
        collection.delete_one({"ticket_id": ticket_id})
        logging.info("Ticket Id deleted")
        return {"successful"}
    else:
        logging.info("Ticket not there")
        return {"ticket id not found"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("varsha:app")
