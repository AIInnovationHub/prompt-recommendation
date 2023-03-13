import sqlite3


class SQLiteDB:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.conn.row_factory = sqlite3.Row
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn is not None:
            self.conn.close()

    def execute(self, sql, params=None):
        cursor = self.conn.cursor()
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        return cursor

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def create_table(self, table_name, columns):
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute(sql).close()

    def drop_table(self, table_name):
        sql = f"DROP TABLE IF EXISTS {table_name}"
        self.execute(sql).close()

    def insert(self, table_name, columns, values):
        placeholders = ', '.join(['?' for _ in values])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute(sql, values).close()

    def update(self, table_name, set_clause, where_clause, params=None):
        sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
        self.execute(sql, params).close()

    def delete(self, table_name, where_clause, params=None):
        sql = f"DELETE FROM {table_name} WHERE {where_clause}"
        self.execute(sql, params).close()

    def select(self, table_name, columns='*', where_clause=None, params=None):
        sql = f"SELECT {columns} FROM {table_name}"
        if where_clause is not None:
            sql += f" WHERE {where_clause}"
        return self.execute(sql, params)
