import sqlite3

conn = sqlite3.connect('./database/app.db')

c = conn.cursor()

'''c.execute("""CREATE TABLE students(
    first text,
    middle text,
    surname text,
    course text
    )""")
'''

conn.commit()
#c.execute("INSERT INTO students values ('AbdulMumin', 'Onoroyiza', 'Adeyemo', 'MAT112')")

c.execute("SELECT * FROM students WHERE first='AbdulMumin'")
print(c.fetchall())

conn.commit()

conn.close()