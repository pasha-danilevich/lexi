from domain.user.repository import UserRepository
from domain.user.schema import UserCreate, UserResponse


class UserService:
    def __init__(self, repo: UserRepository = UserRepository()):
        self.repo = repo

    async def create(self, data: UserCreate):
        hashed_password = "hashed_" + data.password  # Пример хеширования
        user = await self.repo.create_user(
            username=data.username,
            email=data.email,
            hashed_password=hashed_password,
        )
        return UserResponse.model_validate(user)
