"""数据库模块：SQLite 内存连接与建表。"""

import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    views INTEGER NOT NULL DEFAULT 0,
    likes INTEGER NOT NULL DEFAULT 0,
    comments INTEGER NOT NULL DEFAULT 0,
    category TEXT
);

CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id INTEGER NOT NULL,
    score REAL NOT NULL,
    level TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (video_id) REFERENCES videos (id)
);
"""


def get_connection() -> sqlite3.Connection:
    """建立 SQLite 内存连接，并让查询结果可以按列名读取。"""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables(conn: sqlite3.Connection) -> None:
    """按 SCHEMA 建表，重复调用不会报错。"""
    conn.executescript(SCHEMA)
    conn.commit()


def init_db() -> sqlite3.Connection:
    """一步拿到建好表的连接，供其他模块调用。"""
    conn = get_connection()
    create_tables(conn)
    return conn


def main() -> None:
    """自测：建连接、建表、插一条数据、读出来。"""
    conn = init_db()

    conn.execute(
        "INSERT INTO videos (title, views, likes, comments, category) VALUES (?, ?, ?, ?, ?)",
        ("AI短视频测试一", 12000, 860, 45, "AI"),
    )
    conn.commit()

    row = conn.execute("SELECT id, title, views, likes, comments FROM videos").fetchone()
    print("插入并读回：", dict(row))

    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    print("已建表：", [t["name"] for t in tables])

    conn.close()


if __name__ == "__main__":
    main()