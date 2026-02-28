from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, UserAge, Feedback

app = FastAPI()

feedbacks: list = []

@app.get("/")
async def read_root():
    return FileResponse("index.html")

@app.post("/calculate")
async def calculate(num1: float, num2: float):
    return {"result": num1 + num2}

@app.get("/users")
async def get_user():
    user = User(name="Богдан Макаров", id=1)
    return user

@app.post("/user")
async def check_adult(user: UserAge):
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.is_adult
    }

@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}