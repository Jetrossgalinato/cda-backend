from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/search")
async def search_user(query: int):
    return {"query": query}

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user": user_id}