import sqlite3


class Proxy:
    def __init__(self, db):
        self.db = db
        self.connection = sqlite3.connect(db)
        self.connection.execute('''
                                       CREATE TABLE IF NOT EXISTS dados(
                                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                                       name TEXT NOT NULL,
                                       score INTEGER NOT NULL)
                                    '''
                                )

    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO dados (name, score) VALUES (:name, :score)', score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()
