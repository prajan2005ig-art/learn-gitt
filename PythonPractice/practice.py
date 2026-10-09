import sqlite3

connection = sqlite3.connect("university.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS university (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")

cursor.execute("""
    INSERT OR IGNORE INTO university (id, name)
    VALUES (1, 'University of Auckland')
""")

cursor.execute("""
    INSERT OR IGNORE INTO university (id, name)
    VALUES (2, 'Victoria University of Wellington')
""")

connection.commit()

print("Uni table created!")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS programmes (
        programme_id INTEGER PRIMARY KEY,
        programme_name TEXT,
        university_id INTEGER,
        FOREIGN KEY (university_id)
        REFERENCES university(id)
    )
""")

connection.commit()

print("Programmes table created!")


cursor.execute("""
    INSERT INTO programmes (programme_name, university_id)
    VALUES ('Master of Artificial Intelligence', 1)
""")

cursor.execute("""
    INSERT INTO programmes (programme_name, university_id)
    VALUES ('Master of Data Science', 1)
""")

cursor.execute("""
    INSERT INTO programmes (programme_name, university_id)
    VALUES ('Master of Artificial Intelligence', 2)
""")

connection.commit()

print("Programmes added!")

connection.close()