import sqlite3
from sqlite3 import Error

class Configure:
    def connect_database(self):
        
        self.conn = None
        
        try:
            self.conn = sqlite3.connect('./database/app.db')
            
        except Error as e:
            print(e)
        self.c = self.conn.cursor()
        
        return self.conn
    
    def create_student(self):
        self.connect_database()
        self.c.execute("""CREATE TABLE IF NOT EXISTS students
        (
            stud_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            firstName TEXT NOT NULL,
            middleName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            gender TEXT NOT NULL,
            phoneNumber TEXT NOT NULL,
            department TEXT NOT NULL,
            matricNo TEXT NOT NULL
            )""")
        self.conn.commit()
        self.conn.close()
        print("Student Table has been created successfully!.")

    def create_course(self, list):
        if self.connect_database():
            self.c.execute("""CREATE TABLE IF NOT EXITS courses
            (
            course_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            stud_ID INTEGER NOT NULL,
            course TEXT NOT NULL
            )""")
            
            self.conn.commit()
        else:
            self.conn.rollback()
        
        self.conn.close()
        print("Course Table has been created successfully!.")

    def insert_stud(self, first, middle, last, department, matric):
        self.connect_database()
        self.c.execute("INSERT INTO students VALUES (?,?,?,?,?)", (first, middle, last, department, matric))
        self.conn.commit()
        self.conn.close()
    
    #Search by the first name in the existing database
    def query_from_database(self, table, item, search):
        self.connect_database()
        try:
            self.c.execute("SELECT * FROM {table} WHERE {item} ='{search}'")
        
        except:
            self.conn.rollback()
        items = self.c.fetchall()

        for item in items:
            print(items)
        self.conn.commit()
        self.conn.close()