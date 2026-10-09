import sqlite3


def create_database():

    connection = sqlite3.connect("admission_predictor.db")

    cursor = connection.cursor()

    # Institutions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS institutions (
            institution_id INTEGER PRIMARY KEY,
            institution_name TEXT NOT NULL UNIQUE,
            institution_type TEXT NOT NULL,
            city TEXT,
            website TEXT
        )
    """)

    # Programmes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS programmes (
            programme_id INTEGER PRIMARY KEY,
            institution_id INTEGER NOT NULL,
            programme_name TEXT NOT NULL,
            field TEXT,
            qualification_level TEXT,
            FOREIGN KEY (institution_id)
            REFERENCES institutions(institution_id)
        )
    """)

    # Study pathways
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_pathways (
            pathway_id INTEGER PRIMARY KEY,
            programme_id INTEGER NOT NULL,
            credits INTEGER NOT NULL,
            duration_years REAL,
            semesters INTEGER,
            eligibility_description TEXT,
            work_experience_required INTEGER DEFAULT 0,
            minimum_experience_years REAL,
            FOREIGN KEY (programme_id)
            REFERENCES programmes(programme_id)
        )
    """)

    # Academic requirements
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS academic_requirements (
            requirement_id INTEGER PRIMARY KEY,
            pathway_id INTEGER NOT NULL,
            minimum_cgpa REAL,
            degree_requirement TEXT,
            subject_requirement TEXT,
            academic_requirement_description TEXT,
            FOREIGN KEY (pathway_id)
            REFERENCES study_pathways(pathway_id)
        )
    """)

    connection.commit()

    connection.close()

    print("Database structure created successfully!")

def add_institutions():

    connection = sqlite3.connect("admission_predictor.db")

    cursor = connection.cursor()

    institutions = [
        (1, "University of Auckland", "University", "Auckland"),
        (2, "Auckland University of Technology", "University", "Auckland"),
        (3, "University of Waikato", "University", "Hamilton"),
        (4, "Massey University", "University", "Palmerston North"),
        (5, "Victoria University of Wellington", "University", "Wellington"),
        (6, "University of Canterbury", "University", "Christchurch"),
        (7, "Lincoln University", "University", "Lincoln"),
        (8, "University of Otago", "University", "Dunedin"),
        (9, "Unitec", "Polytechnic", "Auckland"),
        (10, "New Zealand School of Education", "Private Tertiary Provider", "Auckland")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO institutions
        (institution_id, institution_name, institution_type, city)
        VALUES (?, ?, ?, ?)
    """, institutions)

    connection.commit()

    connection.close()

    print("Institutions added successfully!")


def show_institutions():

    connection = sqlite3.connect("admission_predictor.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM institutions
    """)

    institutions = cursor.fetchall()

    for institution in institutions:
        print(institution)

    connection.close()

def add_programmes():

    connection = sqlite3.connect("admission_predictor.db")

    cursor = connection.cursor()

    programmes = [

        # University of Auckland
        (1, 1, "Master of Artificial Intelligence",
         "Artificial Intelligence", "Level 9"),

        (2, 1, "Master of Data Science",
         "Data Science", "Level 9"),

        (3, 1, "Master of Information Technology",
         "Information Technology", "Level 9"),


        # Auckland University of Technology
        (4, 2, "Master of Applied Artificial Intelligence",
         "Artificial Intelligence", "Level 9"),

        (5, 2, "Master of Computer and Information Sciences",
         "Computer Science / Information Technology", "Level 9"),


        # University of Waikato
        (6, 3, "Master of Artificial Intelligence",
         "Artificial Intelligence", "Level 9"),

        (7, 3, "Master of Data Science",
         "Data Science", "Level 9"),

        (8, 3, "Master of Information Technology",
         "Information Technology", "Level 9"),


        # Massey University
        (9, 4, "Master of Information Sciences",
         "Information Sciences", "Level 9"),


        # Victoria University of Wellington
        (10, 5, "Master of Artificial Intelligence",
         "Artificial Intelligence", "Level 9"),

        (11, 5, "Master of Data Science",
         "Data Science", "Level 9"),


        # University of Canterbury
        (12, 6, "Master of Artificial Intelligence",
         "Artificial Intelligence", "Level 9"),

        (13, 6, "Master of Applied Data Science",
         "Data Science", "Level 9"),


        # Lincoln University
        (14, 7, "Master of Applied Computing",
         "Computing", "Level 9"),


        # University of Otago
        (15, 8, "Master of Science (Applied) in Computer Science",
         "Computer Science", "Level 9"),

        (16, 8, "Master of Science (Applied) in Data Science",
         "Data Science", "Level 9"),


        # Unitec
        (17, 9, "Master of Applied Technologies - Computing",
         "Computing", "Level 9"),


        # New Zealand School of Education
        (18, 10, "Master of Data Analytics",
         "Data Analytics", "Level 9"),

        (19, 10, "Master of Business Intelligence",
         "Business Intelligence", "Level 9")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO programmes
        (
            programme_id,
            institution_id,
            programme_name,
            field,
            qualification_level
        )
        VALUES (?, ?, ?, ?, ?)
    """, programmes)

    connection.commit()

    connection.close()

    print("Programmes added successfully!")
add_programmes()

def show_programmes():

    connection = sqlite3.connect("admission_predictor.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            institutions.institution_name,
            programmes.programme_name,
            programmes.field,
            programmes.qualification_level

        FROM institutions

        JOIN programmes
        ON institutions.institution_id = programmes.institution_id
    """)

    programmes = cursor.fetchall()

    for programme in programmes:
        print(programme)

    connection.close()

def add_pathways():

    connection = sqlite3.connect("admission_predictor.db")

    cursor = connection.cursor()

    pathways = [

        # ==========================================
        # UNIVERSITY OF AUCKLAND
        # ==========================================

        # Master of Artificial Intelligence
        (
            1, 1, 120, 1.0, 2,
            "Taught 120-point pathway",
            0, None
        ),

        (
            2, 1, 180, 1.5, 3,
            "Taught 180-point pathway",
            0, None
        ),


        # Master of Data Science
        (
            3, 2, 180, 1.5, 3,
            "Taught 180-point pathway",
            0, None
        ),

        (
            4, 2, 240, 2.0, 4,
            "Taught 240-point pathway",
            0, None
        ),


        # Master of Information Technology
        (
            5, 3, 120, 1.0, 2,
            "Taught 120-point pathway",
            0, None
        ),

        (
            6, 3, 180, 1.5, 3,
            "Taught 180-point pathway",
            0, None
        ),

        (
            7, 3, 240, 2.0, 4,
            "Taught 240-point pathway",
            0, None
        ),


        # ==========================================
        # AUT
        # ==========================================

        # Master of Applied Artificial Intelligence
        (
            8, 4, 180, 1.5, 3,
            "Standard 180-point pathway",
            0, None
        ),

        # Master of Computer and Information Sciences
        (
            9, 5, 180, 1.5, 3,
            "Standard 180-point pathway",
            0, None
        ),


        # ==========================================
        # UNIVERSITY OF WAIKATO
        # ==========================================

        # Master of Artificial Intelligence
        (
            10, 6, 180, 1.5, 3,
            "Standard 180-point pathway",
            0, None
        ),

        # Master of Data Science
        (
            11, 7, 180, 1.5, 3,
            "Standard 180-point pathway",
            0, None
        ),

        # Master of Information Technology
        (
            12, 8, 120, 1.0, 2,
            "120-point pathway",
            0, None
        ),

        (
            13, 8, 180, 1.5, 3,
            "180-point pathway",
            0, None
        ),

        (
            14, 8, 240, 2.0, 4,
            "240-point pathway",
            0, None
        ),


        # ==========================================
        # MASSEY UNIVERSITY
        # ==========================================

        # Master of Information Sciences
        (
            15, 9, 180, 1.5, 3,
            "Professional pathway",
            0, None
        ),

        (
            16, 9, 180, 1.5, 3,
            "Research pathway",
            0, None
        ),

        (
            17, 9, 120, 1.0, 2,
            "120-credit thesis advanced-entry pathway",
            0, None
        ),


        # ==========================================
        # VICTORIA UNIVERSITY OF WELLINGTON
        # ==========================================

        # Master of Artificial Intelligence
        (
            18, 10, 180, 1.0, 3,
            "Standard 180-point pathway",
            0, None
        ),

        # Master of Data Science
        (
            19, 11, 240, 2.0, 6,
            "Standard 240-point pathway",
            0, None
        ),

        (
            20, 11, 180, 1.0, 3,
            "Reduced pathway for students receiving prior-study exemption",
            0, None
        ),


        # ==========================================
        # UNIVERSITY OF CANTERBURY
        # ==========================================

        # Master of Artificial Intelligence
        (
            21, 12, 180, 1.5, 3,
            "Standard 180-point pathway",
            0, None
        ),

        # Master of Applied Data Science
        (
            22, 13, 180, 1.5, 3,
            "Standard 180-point pathway",
            0, None
        ),


        # ==========================================
        # LINCOLN UNIVERSITY
        # ==========================================

        # Master of Applied Computing
        (
            23, 14, 180, 1.5, 3,
            "Standard 180-credit pathway",
            0, None
        ),


        # ==========================================
        # UNIVERSITY OF OTAGO
        # ==========================================

        # MSc Applied Computer Science
        (
            24, 15, 180, 1.0, 2,
            "Master of Science (Applied) pathway",
            0, None
        ),

        # MSc Applied Data Science
        (
            25, 16, 180, 1.5, 3,
            "Master of Science (Applied) pathway",
            0, None
        ),


        # ==========================================
        # UNITEC
        # ==========================================

        # Master of Applied Technologies - Computing
        (
            26, 17, 180, 1.5, 3,
            "Standard 180-credit pathway",
            0, None
        ),


        # ==========================================
        # NZSE
        # ==========================================

        # Master of Data Analytics
        (
            27, 18, 180, 1.1, 3,
            "Standard 180-credit pathway",
            0, None
        ),

        # Master of Business Intelligence
        (
            28, 19, 180, 1.1, 3,
            "Standard 180-credit pathway",
            0, None
        )
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO study_pathways
        (
            pathway_id,
            programme_id,
            credits,
            duration_years,
            semesters,
            eligibility_description,
            work_experience_required,
            minimum_experience_years
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, pathways)

    connection.commit()

    connection.close()

    print("Study pathways added successfully!")

def show_pathways():

    connection = sqlite3.connect("admission_predictor.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            institutions.institution_name,
            programmes.programme_name,
            study_pathways.credits,
            study_pathways.duration_years,
            study_pathways.semesters,
            study_pathways.eligibility_description

        FROM institutions

        JOIN programmes
        ON institutions.institution_id = programmes.institution_id

        JOIN study_pathways
        ON programmes.programme_id = study_pathways.programme_id
    """)

    pathways = cursor.fetchall()

    for pathway in pathways:
        print(pathway)

    connection.close()
