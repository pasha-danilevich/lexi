from fastapi import FastAPI, Depends, HTTPException, APIRouter
from authx import AuthX, AuthXConfig

router = APIRouter(prefix="/auth", tags=["Авторизация"])

config = AuthXConfig()
config.JWT_ALGORITHM = "HS256"
config.JWT_SECRET_KEY = "SECRET_KEY"

security = AuthX(config=config)


@router.get("/login")
def login(username: str, password: str):
    if username == "test" and password == "test":
        token = security.create_access_token(uid=username)
        return {"access_token": token}
    raise HTTPException(401, detail={"message": "Bad credentials"})


@router.get("/protected", dependencies=[Depends(security.access_token_required)])
def get_protected():
    return {"message": "Hello World"}
