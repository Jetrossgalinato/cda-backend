from fastapi import FastAPI
from api.users import router as users_router

app = FastAPI()

app.include_router(users_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "This is the about API!"}

