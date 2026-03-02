from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "This is the about API!"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user": user_id}

@app.get("/users/search")
async def search_user(query: str):
    return {"query": query}