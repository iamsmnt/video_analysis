from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.auth.hashing import hash_password
from app.database.session import get_session
from app.models.user import User

router = APIRouter()

@router.post("/register")
async def register_user(username: str, password: str, role: str = "user", db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(User).where(User.username == username))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(username=username, password=hash_password.bcrypt(password), role=role)
    db.add(new_user)
    await db.commit()
    return {"msg": "User registered successfully"}