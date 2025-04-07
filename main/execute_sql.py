from django.shortcuts import render
from django.db import connection

def execute_sql_query(sql_query, params=None):
    """Execute raw SQL query and return the results."""
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            if sql_query.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                return results
            else:
                return None
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None
