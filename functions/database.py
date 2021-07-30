import sqlite3


def create_connection():
    return sqlite3.connect('database/EnglishDictionary/Dictionary.db')

def get_query(strQuery):
    with create_connection() as conn:
        return conn.execute(strQuery)