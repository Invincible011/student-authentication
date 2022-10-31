import sqlite3
from sqlite3 import Error

class Configure:
    
    conn = None
    
    def connect_database(self):
        
        try:
            self.conn = sqlite3.connect('./database/app.db')
            
        except Error as e:
            print(e)
            
        self.c = self.conn.cursor()
        return self.conn
    
    def create_student(self):
        with self.connect_database():
            try:
                self.c.execute("""CREATE TABLE IF NOT EXISTS students
                (
                    stud_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstName TEXT NOT NULL,
                    middleName TEXT NOT NULL,
                    lastName TEXT NOT NULL,
                    gender TEXT NOT NULL,
                    phoneNumber TEXT NOT NULL,
                    department TEXT NOT NULL
                    )""")
                
                print("Student Table has been created successfully!.")
                
            except:
                self.conn.rollback()

    def create_course(self, list):
        with self.connect_database():
            try:
                self.c.execute("""CREATE TABLE IF NOT EXITS courses
                (
                course_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                stud_ID INTEGER NOT NULL,
                course TEXT NOT NULL
                )""")
                
                print("Course Table has been created successfully!.")
            
            except:
                self.conn.rollback()

    def insert_stud(self, first, middle, last, department, matric):
        with self.connect_database():
            try:
                self.c.execute("INSERT INTO students VALUES (?,?,?,?,?)", (first, middle, last, department, matric))
                
            except:
                self.conn.rollback()
                 
    #Search by the first, last or other possible query from the existing database
    def query_from_database(self, table, item, search):
        with self.connect_database():
            self.c.execute("SELECT * FROM {table} WHERE {item} ='{search}'")            
            
            items = self.c.fetchall()
            for item in items:
                print(item)
    
    def update_stud(self):
        pass
    
    def alter_changes(self):
        pass
    
    def update_course_list(self):
        pass
    
    def add_new_col_student(self):
        pass
    
    def delete_table(self, table):
        with self.connect_database():
            try:
                self.c.execute("DROP TABLE IF EXIS {table}")
                            
            except:
                self.conn.rollback()