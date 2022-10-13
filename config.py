import sqlite3

class Configure:
    def connect_database(self):
        self.conn = sqlite3.connect('./database/app.db')
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE students(
            first text,
            middle text,
            surname text,
            course text
            )""")
        self.conn.commit()
    
    def insert_into_database(self):
        self.c.execute("INSERT INTO students VALUES ('AbdulMumin', 'Onoroyiza', 'Adeyemo', 'MAT112')")
        self.conn.commit()
    
    def query_from_database(self, query, database, search):
        self.c.execute("SELECT {self.query} FROM {self.database} WHERE first='{self.search}'")
        print(self.c.fetchall())
        self.conn.commit()

    def exit_database(self):
        self.conn.close()