from fastapi import FastAPI

app = FastAPI()

# Root route
@app.get("/")
def home():
    return {"message": "StallX Backend Running 🚀"}


# Test route
@app.get("/test")
def test():
 from fastapi import FastAPI
from database import orders_collection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend + DB Connected 🚀"}


# 🔥 TEST INSERT
@app.get("/add-test")
def add_test():
    orders_collection.insert_one({
        "test": "Hello MongoDB"
    })
    return {"status": "Inserted"}