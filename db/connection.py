import os
import psycopg2
from psycopg2 import pool
from contextlib import contextmanager

# Use environment variables or hardcoded values
DB_CONFIG = {
    "database": os.getenv("DB_NAME", "postgres"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASS", "postgres"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
}

# Connection pool
connection_pool = None

def init_connection_pool(minconn=1, maxconn=10):
    global connection_pool
    if not connection_pool:
        connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn,
            maxconn,
            **DB_CONFIG
        )
        print("✅ PostgreSQL connection pool created")
    else:
        print("⚠️ Connection pool already initialized")

def close_connection_pool():
    global connection_pool
    if connection_pool:
        connection_pool.closeall()
        print("🔒 Connection pool closed")

@contextmanager
def get_db_connection():
    global connection_pool
    if not connection_pool:
        raise Exception("Connection pool is not initialized.")
    conn = connection_pool.getconn()
    try:
        yield conn
    finally:
        connection_pool.putconn(conn)
