import traceback
from fastapi import Request
from fastapi.templating import Jinja2Templates
from Schemas.models import user
from script.core.logging.logs.logger import logging
from script.core.db.mongo_utility import mongo

templates = Jinja2Templates(directory="templates")

async def user_signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


async def delete_ticket(request: Request):
    return templates.TemplateResponse("delete.html", {"request": request})


async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


async def update_ticket(request: Request):
    return templates.TemplateResponse("update_ticket.html", {"request": request})


async def ticket_reserve(request: Request):
    return templates.TemplateResponse("ticket_reservation.html", {"request": request})


async def signup(request: Request):
    data = await request.form()
    logging.debug('signup')
    var = user(
        username=data["username"],
        password=data["password"],
        email=data["email"]
    )
    mongo.for_insert_one("varsha", var)
    if user:
        logging.debug("Sign up page created successfully")
        return {"message": "Sign up successful"}
    else:
        return {"message": "none"}

async def login1(request: Request):
    data = await request.form()
    username = data["username"]
    password = data["password"]
    find = {"username": username, "password": password}
    var = mongo.for_find_one("varsha", find)
    if var:
        logging.debug('login successful')
        return templates.TemplateResponse("ticket_reservation.html", {"request": request})
    else:
        logging.debug('not successful')
        return {"error": "Login failed, username or password is wrong!!"}

async def ticket_reserved1(request: Request):
    try:
        data = await request.form()
        ticket_id = data["ticket_id"]
        origin = data["origin"]
        destination = data["destination"]
        date = data["date"]
        find = {"ticket_id": ticket_id}
        var = mongo.for_find_one("varsha", find)
        if var:
            logging.debug('Ticket already Exist')
            print(var)
            return {"message": "Not possible"}
        else:
            insert = {"ticket_id": ticket_id, "origin": origin, "destination": destination, "date": date}
            print(insert)
            var_1 = mongo.for_insert_one("varsha", insert)
            if var_1:
                logging.debug('Ticket Created successful')
                return {"message": "Successfully"}
            else:
                logging.debug('Ticket not created successful')
                return {"error": "Not successful"}
    except Exception as e:
        traceback.print_exc()
        return {'error', str(e)}

async def update_ticket1(request: Request):
    data = await request.form()
    ticket_id = data["ticket_id"]
    date = data["date"]
    update = {"ticket_id": ticket_id}
    set = {"$set": {"date": date}}
    user_1 = mongo.for_update_one("varsha", update, set)
    if user_1:
        logging.debug("Date updated Successfully")
        return {"successful"}
    else:
        logging.debug("Update failed")
        return {"message": "date not updated"}


async def delete_ticket1(request: Request):
    data = await request.form()
    ticket_id = data["ticket_id"]
    # origin = data["origin"]
    # destination = data["destination"]
    find = {"ticket_id": ticket_id}
    delete_ticket_1 = mongo.for_find_one("varsha", find)
    if delete_ticket_1:
        delete = {"ticket_id": ticket_id}
        mongo.for_delete_one("varsha", delete)
        logging.debug("Ticket Id deleted")
        return {"successful"}
    else:
        logging.debug("Ticket not there")
        return {"ticket id not found"}
