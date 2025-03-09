from domain.user.model import User


class UserRepository:
    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        return await User.filter(id=user_id).first()

    @staticmethod
    async def create_user(username: str, email: str, hashed_password: str) -> User:
        return await User.create(
            username=username, email=email, hashed_password=hashed_password
        )


class MockUserRepository:
    @staticmethod
    async def create_user(
        self, username: str, email: str, hashed_password: str
    ) -> dict:
        return {"username": username, "email": email}
