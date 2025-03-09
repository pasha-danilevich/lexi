from fastapi import APIRouter

from api.auth.api import router as auth_router
from api.user.api import router as user_router
from api.word.api import router as word_router


PREFIX = ""

router = APIRouter(prefix=PREFIX)

router.include_router(auth_router)
router.include_router(user_router)
router.include_router(word_router)
