import psycopg2
import streamlit as st
from typing import List, Any
import hashlib

CONN_STR = st.secrets["NEONDB_CONNECTION_STRING"]

def init_db():
    """
    Connect to NeonDB (Postgres) and create tables if they don't exist.
    """
    with psycopg2.connect(CONN_STR) as conn:
        conn.autocommit = True
        with conn.cursor() as cursor:
            # Enable pgvector extension (used for RAG in rag.py)
            cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")

            # Create table for users
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Create table for chat logs
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS chat_logs (
                    id SERIAL PRIMARY KEY,
                    user_role TEXT NOT NULL,
                    user_message TEXT NOT NULL,
                    bot_response TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

def create_user(username: str, password: str, role: str):
    with psycopg2.connect(CONN_STR) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (username, password, role)
                VALUES (%s, %s, %s)
            """, (username, password, role))

def get_user(username: str):
    with psycopg2.connect(CONN_STR) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            return cursor.fetchone()

def log_chat(user_role: str, user_message: str, bot_response: str):
    with psycopg2.connect(CONN_STR) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO chat_logs (user_role, user_message, bot_response)
                VALUES (%s, %s, %s)
            """, (user_role, user_message, bot_response))

def fetch_chat_logs() -> List[Any]:
    with psycopg2.connect(CONN_STR) as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, user_role, user_message, bot_response, timestamp
                FROM chat_logs
                ORDER BY timestamp DESC
            """)
            return cursor.fetchall()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
