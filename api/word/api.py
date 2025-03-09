from fastapi import APIRouter

router = APIRouter(prefix="/word", tags=["Слова"])


@router.post("/")
async def create_user():
    return dict(status="success")
