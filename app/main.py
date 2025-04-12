from fastapi import FastAPI
from app.routes import users
from app.database.session import engine
from app.models.user import Base

# Create tables if they don't exist (for dev only — use Alembic in production)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Video App - Users Only",
    version="1.0.0",
)

# Include users route
app.include_router(users.router, prefix="/users", tags=["Users"])
