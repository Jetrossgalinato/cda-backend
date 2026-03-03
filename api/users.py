from fastapi import APIRouter

router = APIRouter()

@router.get("/users/search")
async def search_user(query: int):
    return {"query": query}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user": user_id}