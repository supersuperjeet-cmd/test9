#!/usr/bin/env python3
"""Simple DB connectivity check for PostgreSQL (Neon/Render)."""
import os
import sys
import psycopg2
from psycopg2 import sql


def main():
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        print("ERROR: DATABASE_URL environment variable is not set.")
        print("Export it like: export DATABASE_URL='postgresql://user:pass@host:5432/dbname'")
        sys.exit(2)

    try:
        conn = psycopg2.connect(dsn)
        conn.autocommit = True
        cur = conn.cursor()

        # Create a simple table if it doesn't exist
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS app_messages (
                id SERIAL PRIMARY KEY,
                content TEXT NOT NULL,
                created_at TIMESTAMPTZ DEFAULT now()
            )
            """
        )

        # Insert a test row
        cur.execute(
            "INSERT INTO app_messages (content) VALUES (%s) RETURNING id, created_at",
            ("db_check: test row",),
        )
        row = cur.fetchone()
        print("Inserted test row id:", row[0], "created_at:", row[1])

        # Read back latest row
        cur.execute(
            sql.SQL("SELECT id, content, created_at FROM app_messages ORDER BY id DESC LIMIT 1")
        )
        latest = cur.fetchone()
        print("Latest row:", latest)

        cur.close()
        conn.close()
        print("SUCCESS: Database connection and read/write test completed.")
    except Exception as e:
        print("ERROR: Could not connect or operate on the database:", str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
