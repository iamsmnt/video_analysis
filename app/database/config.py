import os
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv

#for local
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL","postgresql+asyncpg://postgres:postgres@localhost/postgres")
engine = create_async_engine(DATABASE_URL, echo=True)
