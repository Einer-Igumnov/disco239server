import sqlite3


class Database:
    def __init__(self, name: str):
        self.conn = sqlite3.connect(name + '.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id TEXT NOT NULL,
        name TEXT NOT NULL,
        class_name TEXT NOT NULL,
        arrived BOOLEAN NOT NULL,
        image_link TEXT
        )
        ''')

    def add_user(self, uid: str, name: str, class_name: str, image_link: str):
        self.cursor.execute('''
            INSERT INTO users (id, name, class_name, arrived, image_link) VALUES (?, ?, ?, ?, ?)
        ''', (uid, name, class_name, False, image_link))
        self.conn.commit()

    def get_user(self, uid: str):
        self.cursor.execute('SELECT name, class_name, arrived, image_link FROM users WHERE id = ?', (uid,))
        results = self.cursor.fetchall()
        if len(results) == 0:
            return {"exists": False}
        user = results[0]
        return {"exists": True, "name": user[0], "class_name": user[1], "arrived": user[2], "image_link": user[3]}

    def mark_user_as_arrived(self, uid: str):
        self.cursor.execute('UPDATE users SET arrived = ? WHERE id = ?', (True, uid))
        self.conn.commit()

    def mark_all_users_as_not_arrived(self):
        self.cursor.execute('UPDATE users SET arrived = ?', (False,))
        self.conn.commit()

    def update_user(self, uid: str, name: str, class_name: str, image_link: str):
        self.cursor.execute('''
            UPDATE users SET name = ?, class_name = ?, arrived = ?, image_link = ? WHERE id = ?
        ''', (name, class_name, False, image_link, uid))
        self.conn.commit()

