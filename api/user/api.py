from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from domain.user.schema import UserResponse, UserCreate
from domain.user.service import UserService

router = APIRouter(prefix="/user", tags=["Пользователь"])


@router.post("/", response_model=UserResponse)
async def create_user(
    service: Annotated[UserCreate, Depends(UserService().create)],
):
    return service
