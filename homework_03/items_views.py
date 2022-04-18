from fastapi import APIRouter

router = APIRouter(tags=["Items"], prefix="/items")

@router.get("")
def get_items():
    return [{"item_id": 1}]