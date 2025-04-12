from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context
import sys
import os

# Include project directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.models import Base  # adjust as needed
from db.database import DATABASE_URL

config = context.config
fileConfig(config.config_file_name)
config.set_main_option("sqlalchemy.url", DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_online():
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        future=True,
    )

    async def do_run_migrations(connection):
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            render_as_batch=True  # Optional: useful for SQLite
        )
        await context.run_migrations()

    import asyncio
    asyncio.run(do_run_migrations(connectable.connect()))

run_migrations_online()
