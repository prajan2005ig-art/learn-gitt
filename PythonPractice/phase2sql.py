import sqlite3
connection = sqlite3.connect('students.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students(id PRIMARY KEY, name TEXT, age INTEGER,cgpa REAL)''')
cursor.execute('''INSERT OR IGNORE INTO students(name,id,age,cgpa) VALUES ('Prajan',106,21,7.00)''')
cursor.execute('''INSERT OR IGNORE INTO students(name,id,age,cgpa) VALUES ('jack',203,23,8.0)''')
connection.commit()
cursor.execute("""UPDATE students SET cgpa = 7.6 ,age = 22 WHERE name = 'Prajan'""")
connection.commit()
cursor.execute("""DELETE FROM students WHERE name = 'jack'""")
connection.commit()
cursor.execute("""SELECT * FROM students """)
students = cursor.fetchall()
for student in students:
    print(student)

connection.close()

