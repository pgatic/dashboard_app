from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
def get_stats():
    return {
        "users": 120,
        "sales": 35,
        "revenue": 1024
    }
