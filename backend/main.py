from fastapi import FastAPI
from database import orders_collection
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request

import random

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🏠 ROOT
@app.get("/")
def home():
    return {"message": "StallX Backend Running 🚀"}


# 🛒 CREATE ORDER

@app.post("/orders")
async def create_order(request: Request):

    print("🔥 RAW REQUEST RECEIVED")
    
    data = await request.json()
    
    print("🔥 DATA:", data)
    # 🛡️ VALIDATION
    if not data.get("user") or not data.get("cart"):
        return {"error": "Invalid access place complete order properly"}

    if len(data.get("cart")) == 0:
        return {"error": "Cart is empty"}

    # 🎟️ Generate token
    token = random.randint(1, 100)

    order = {
        "orderId": "ORD" + str(random.randint(1000, 9999)),
        "user": data.get("user"),
        "cart": data.get("cart"),
        "token": token,
        "status": "QUEUE",
        "otp": "1234",
        "createdAt": str(datetime.now())
    }

    orders_collection.insert_one(order)

    return {
        "message": "Order created",
        "orderId": order["orderId"],
        "token": token
    }


# 📦 GET ALL ORDERS
@app.get("/orders")
def get_orders():
    orders = list(orders_collection.find({}, {"_id": 0}))
    return orders


# 🔍 GET ORDER BY PHONE
@app.get("/orders/phone/{phone}")
def get_order_by_phone(phone: str):
    order = orders_collection.find_one(
        {"user.phone": phone},
        {"_id": 0}
    )

    if not order:
        return {"error": "Order not found"}

    return order


# 🔄 UPDATE STATUS
@app.put("/orders/{orderId}/status")
def update_status(orderId: str, data: dict):

    status = data.get("status")

    orders_collection.update_one(
        {"orderId": orderId},
        {"$set": {"status": status}}
    )

    return {"message": "Status updated"}


# 🔐 VERIFY OTP
@app.post("/orders/{orderId}/verify-otp")
def verify_otp(orderId: str, data: dict):

    otp = data.get("otp")

    order = orders_collection.find_one({"orderId": orderId})

    if not order:
        return {"error": "Order not found"}

    if order["otp"] != otp:
        return {"error": "Invalid OTP"}

    orders_collection.update_one(
        {"orderId": orderId},
        {"$set": {"status": "COMPLETED"}}
    )

    return {"message": "Order completed"}