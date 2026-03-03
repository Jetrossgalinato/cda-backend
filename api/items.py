from fastapi import APIRouter
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("")
async def create_item(item: Item):
    return {"message": "Item received!", "item_date": item}
