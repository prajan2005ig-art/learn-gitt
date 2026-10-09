import sqlite3

# Connect to database
connection = sqlite3.connect("university.db")

# Create cursor
cursor = connection.cursor()


# -----------------------------
# UNIVERSITY TABLE
# -----------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS university (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")

# Insert universities
cursor.execute("""
    INSERT OR IGNORE INTO university (id, name)
    VALUES (1, 'University of Auckland')
""")

cursor.execute("""
    INSERT OR IGNORE INTO university (id, name)
    VALUES (2, 'Victoria University of Wellington')
""")

connection.commit()

print("University table created!")


# -----------------------------
# PROGRAMMES TABLE
# -----------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS programmes (
        programme_id INTEGER PRIMARY KEY,
        programme_name TEXT,
        id INTEGER,

        FOREIGN KEY (id)
        REFERENCES university(id)
    )
""")

connection.commit()

print("Programmes table created!")


# -----------------------------
# INSERT PROGRAMMES
# -----------------------------

cursor.execute("""
    INSERT INTO programmes (programme_name, id)
    VALUES ('Master of Artificial Intelligence', 1)
""")

cursor.execute("""
    INSERT INTO programmes (programme_name, id)
    VALUES ('Master of Data Science', 1)
""")

cursor.execute("""
    INSERT INTO programmes (programme_name, id)
    VALUES ('Master of Artificial Intelligence', 2)
""")

connection.commit()

print("Programmes added!")


# Close connection
connection.close()