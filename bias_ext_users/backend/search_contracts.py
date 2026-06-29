from __future__ import annotations


def search_index_definitions():
    return (
        {
            "name": "users_profile_fts_idx",
            "drop": "DROP INDEX CONCURRENTLY IF EXISTS users_profile_fts_idx",
            "create": """
                CREATE INDEX CONCURRENTLY IF NOT EXISTS users_profile_fts_idx
                ON users
                USING GIN (
                    to_tsvector(
                        'simple',
                        coalesce(username, '') || ' ' || coalesce(display_name, '') || ' ' || coalesce(bio, '')
                    )
                )
            """,
            "description": "为用户名称、显示名和简介提供 PostgreSQL 全文搜索索引。",
        },
    )
