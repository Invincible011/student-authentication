import sqlite3

class Configure:
    def connect_database(self):
        self.conn = sqlite3.connect('./database/app.db')
        self.c = self.conn.cursor()
    
    def create_student(self):
        self.connect_database()
        self.c.execute("""CREATE TABLE students
        (
            firstName text NOT NULL,
            middleName text NOT NULL,
            lastNAme text NOT NULL,
            department text NOT NULL,
            matric_no text 
            )""")
        self.conn.commit()
        self.conn.close()

    def create_course(self, list):
        if self.connect_database():
            self.c.execute("""CREATE TABLE courses
            (
            Id NOT NULL,
            course NOT NULL,
            matric_no text NOY NULL
            )""")

        else:
            raise f"Cannot connect into the database!!!"
        self.conn.commit()
        self.conn.close()

    def insert_stud(self, first, middle, last, department, matric):
        self.connect_database()
        self.c.execute("INSERT INTO students VALUES (?,?,?,?,?)", (first, middle, last, department, matric))
        self.conn.commit()
        self.conn.close()
    
    #Search by the first name in the existing database
    def query_from_database(self, query, table, item, search):
        self.connect_database()
        self.c.execute("SELECT * FROM {self.table} WHERE {item} ='{self.search}'")
        items = self.c.fetchall()

        for item in items:
            print(items)
        self.conn.commit()
        self.conn.close()