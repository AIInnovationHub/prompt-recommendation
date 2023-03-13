import sqlite3
from typing import List
from user import User


class UserRepository:
    def __init__(self, db_file: str):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
            (user_id TEXT PRIMARY KEY,
             username TEXT NOT NULL,
             password TEXT NOT NULL,
             age INTEGER,
             gender TEXT)''')
        self.conn.commit()

    def add_user(self, user: User):
        c = self.conn.cursor()
        c.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?)',
                  (user.user_id, user.username, user.password, user.age, user.gender))
        self.conn.commit()

    def get_user_by_id(self, user_id: str) -> User:
        c = self.conn.cursor()
        c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        row = c.fetchone()
        if row is not None:
            return User(*row)
        else:
            return None

    def get_all_users(self) -> List[User]:
        c = self.conn.cursor()
        c.execute('SELECT * FROM users')
        rows = c.fetchall()
        return [User(*row) for row in rows]

    def update_user(self, user: User):
        c = self.conn.cursor()
        c.execute('UPDATE users SET username = ?, password = ?, age = ?, gender = ? WHERE user_id = ?',
                  (user.username, user.password, user.age, user.gender, user.user_id))
        self.conn.commit()

    def delete_user(self, user_id: str):
        c = self.conn.cursor()
        c.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
