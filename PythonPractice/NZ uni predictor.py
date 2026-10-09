# ============================================================
# NEW ZEALAND UNIVERSITY ADMISSION PREDICTOR
# PHASE 1 - UNIVERSITY DATA + REQUIREMENT CHECKER
# ============================================================


# ============================================================
# 1. UNIVERSITY DATABASE
# ============================================================

universities = {

    # ========================================================
    # UNIVERSITY OF AUCKLAND
    # ========================================================

    "University of Auckland": {

        "Master of Artificial Intelligence": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1 - 1.5 years",

            "credits": "120 or 180 points",

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Bachelor of Advanced Science (Honours)",
                    "Bachelor of Engineering",
                    "Bachelor of Engineering (Honours)",
                    "Bachelor of Science (Honours)",
                    "Bachelor of Science"
                ],

                "academic_requirement":
                    "GPA/GPE 4.0 or higher depending on pathway",

                "minimum_gpa": 4.0,

                "minimum_grade": None,

                "prerequisites":
                    "Relevant Computer Science, Engineering, Science or related background"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "PTE Academic"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "120-point or 180-point pathway depending on academic background",

            "source":
                "Official University of Auckland programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Data Science": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1 - 2 years",

            "credits": "180 or 240 points",

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Data Science",
                    "Computer Science",
                    "Statistics",
                    "Relevant Science background"
                ],

                "academic_requirement":
                    "Programme pathway and prerequisite requirements apply",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "Relevant background in data science, computer science, statistics or science depending on pathway"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "PTE Academic"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "180-point and 240-point pathways",

            "source":
                "Official University of Auckland programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Information Technology": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1 - 2 years",

            "credits": "120, 180 or 240 points",

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Information Technology",
                    "Computer Science",
                    "Engineering",
                    "Relevant discipline"
                ],

                "academic_requirement":
                    "Programme pathway-specific GPA requirement",

                "minimum_gpa": 4.5,

                "minimum_grade": None,

                "prerequisites":
                    "Depends on selected pathway"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "PTE Academic"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "120, 180 and 240-point pathways",

            "source":
                "Official University of Auckland programme information",

            "last_verified":
                "2026-10-07"
        }
    },


    # ========================================================
    # UNIVERSITY OF CANTERBURY
    # ========================================================

    "University of Canterbury": {

        "Master of Artificial Intelligence": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "18 months",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Computer Science",
                    "Software Engineering",
                    "Computer Engineering",
                    "Related field"
                ],

                "academic_requirement":
                    "B average in 60 points of relevant 300-level COSC, SENG, ENCE or DATA courses",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant 300-level study or approved alternative pathway"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "Other approved tests"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "120 points taught study + 60-point practical project",

            "source":
                "Official University of Canterbury programme information",

            "last_verified":
                "2026-10-07"
        },


        "Professional Master of Computer Science": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1 year",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Computer Science",
                    "Computer Engineering",
                    "Software Engineering",
                    "Similar field"
                ],

                "academic_requirement":
                    "Relevant bachelor's degree with required academic performance",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant computing background or approved professional experience"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "Other approved tests"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "Professional postgraduate computer science programme",

            "source":
                "Official University of Canterbury programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Software Engineering": {

            "status": "Subject to programme approval / availability",

            "qualification_level": 9,

            "duration": "Approximately 1.5 years",

            "credits": 180,

            "intakes": ["Check current intake"],

            "eligibility": {

                "degree_background": [
                    "Computer Science",
                    "Software Engineering",
                    "Related computing field"
                ],

                "academic_requirement":
                    "Relevant bachelor's degree and programme-specific requirements",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "Relevant software engineering preparation"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": True,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "Includes significant software engineering practical requirements",

            "source":
                "Official University of Canterbury programme information",

            "last_verified":
                "2026-10-07"
        }
    },


    # ========================================================
    # UNIVERSITY OF WAIKATO
    # ========================================================

    "University of Waikato": {

        "Master of Artificial Intelligence": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1.5 years",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Computer Science",
                    "Computer Engineering",
                    "Bachelor of Science",
                    "Relevant equivalent qualification"
                ],

                "academic_requirement":
                    "At least B average across relevant 300-level papers",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Required preparation for graduate AI study"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "PTE Academic"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "180-point master's programme",

            "source":
                "Official University of Waikato programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Data Science": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1 - 1.5 years",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Computing",
                    "Data Science",
                    "Science",
                    "Mathematics",
                    "Statistics",
                    "Relevant background"
                ],

                "academic_requirement":
                    "At least B average in relevant 300-level or higher majoring papers",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant academic preparation"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "PTE Academic"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "Includes optional areas such as AI, Business Analytics, GIS, Health Analytics, Mathematics and Statistical Modelling",

            "source":
                "Official University of Waikato programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Information Technology": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1 - 2 years",

            "credits": "120, 180 or 240 points",

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Information Technology",
                    "Computer Science",
                    "Relevant field"
                ],

                "academic_requirement":
                    "Recognised bachelor's degree with required academic preparation",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "Programme-specific requirements apply"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "PTE Academic"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "May include industry internship and project-based study",

            "source":
                "Official University of Waikato programme information",

            "last_verified":
                "2026-10-07"
        }
    },


    # ========================================================
    # VICTORIA UNIVERSITY OF WELLINGTON
    # ========================================================

    "Victoria University of Wellington": {

        "Master of Artificial Intelligence": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "3 trimesters",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Computer Science",
                    "Related discipline"
                ],

                "academic_requirement":
                    "Bachelor's degree with at least a B average in relevant final-year courses",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant computing/AI preparation"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "PTE Academic"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "180-point master's programme",

            "source":
                "Official Victoria University of Wellington programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Computer Science": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "3 trimesters",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Computer Science",
                    "Related field"
                ],

                "academic_requirement":
                    "Bachelor's degree with at least a B average or approved professional experience",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant computer science preparation"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "PTE Academic"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "180-point postgraduate computer science qualification",

            "source":
                "Official Victoria University of Wellington programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Data Science": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "Approximately 5 - 6 trimesters",

            "credits": 240,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Data Science",
                    "Computer Science",
                    "Statistics",
                    "Related field"
                ],

                "academic_requirement":
                    "Bachelor's degree with normally a B+ average in relevant subjects",

                "minimum_gpa": None,

                "minimum_grade": "B+",

                "prerequisites":
                    "Relevant data science, computer science or statistics background"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": [
                    "TOEFL iBT",
                    "PTE Academic"
                ]
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "240 points; exemptions may reduce study time for students with appropriate prior study",

            "source":
                "Official Victoria University of Wellington programme information",

            "last_verified":
                "2026-10-07"
        },


        # ====================================================
        # SCHOOL OF EDUCATION
        # ====================================================

        "Master of Education": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "3 trimesters",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Education",
                    "Psychology",
                    "Teacher Education",
                    "Related discipline"
                ],

                "academic_requirement":
                    "Relevant bachelor's degree and programme-specific academic requirements",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "Education or related academic/teaching background"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "180-point postgraduate education programme",

            "source":
                "Victoria University of Wellington School of Education",

            "last_verified":
                "2026-10-07"
        },


        "Master of Teaching and Learning - Primary": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "3 trimesters",

            "credits": 180,

            "intakes": ["February"],

            "eligibility": {

                "degree_background": [
                    "Bachelor's degree"
                ],

                "academic_requirement":
                    "Bachelor's degree with GPA 6.5 or above plus selection requirements",

                "minimum_gpa": 6.5,

                "minimum_grade": None,

                "prerequisites":
                    "Literacy, numeracy, selection/interview and Teaching Council-related requirements"
            },

            "english": {

                "IELTS": 7.0,

                "minimum_band": 7.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "Teacher education programme with practical teaching requirements",

            "source":
                "Victoria University of Wellington School of Education",

            "last_verified":
                "2026-10-07"
        },


        "Master of Teaching and Learning - Secondary": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "3 trimesters",

            "credits": 180,

            "intakes": ["February"],

            "eligibility": {

                "degree_background": [
                    "Bachelor's degree in a teachable subject"
                ],

                "academic_requirement":
                    "Bachelor's degree and programme-specific selection requirements",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "Suitable secondary teaching subject background and selection requirements"
            },

            "english": {

                "IELTS": 7.0,

                "minimum_band": 7.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "Secondary teacher education with professional teaching practice",

            "source":
                "Victoria University of Wellington School of Education",

            "last_verified":
                "2026-10-07"
        }
    },


    # ========================================================
    # UNIVERSITY OF OTAGO
    # ========================================================

    "University of Otago": {

        "Master of Science (Coursework) - Computer Science": {

            "status": "Active / 2027 programme",

            "qualification_level": 9,

            "duration": "12 - 18 months",

            "credits": "120 or 180 points",

            "intakes": ["February"],

            "eligibility": {

                "degree_background": [
                    "Computer Science",
                    "Relevant subject"
                ],

                "academic_requirement":
                    "At least B average in relevant 300-level papers",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant 300-level study"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "120-point or 180-point coursework pathways",

            "source":
                "Official University of Otago programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Science (Applied) - Computer Science": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "12 - 18 months",

            "credits": 180,

            "intakes": ["February"],

            "eligibility": {

                "degree_background": [
                    "Computer Science",
                    "Related computing field"
                ],

                "academic_requirement":
                    "Relevant bachelor's degree with required academic performance",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant computer science preparation"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "Applied postgraduate computer science programme",

            "source":
                "Official University of Otago programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Science (Applied) - Data Science": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "12 - 18 months",

            "credits": 180,

            "intakes": ["February"],

            "eligibility": {

                "degree_background": [
                    "Data Science",
                    "Statistics",
                    "Computer Science",
                    "Related field"
                ],

                "academic_requirement":
                    "Relevant academic background with required academic performance",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant data science/statistics/computing preparation"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "Includes machine learning, statistical modelling, AI, data management and high-performance computing",

            "source":
                "Official University of Otago programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Digital Technologies": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "Programme-specific",

            "credits": "Programme-specific",

            "intakes": ["Check current intake"],

            "eligibility": {

                "degree_background": [
                    "Computer Science",
                    "Information Science",
                    "Data Science",
                    "Statistics"
                ],

                "academic_requirement":
                    "Relevant bachelor's degree plus at least 3 years relevant professional experience",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "At least 3 years relevant professional experience"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": True,

                "minimum_years": 3
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "Professional digital technology qualification",

            "source":
                "Official University of Otago programme information",

            "last_verified":
                "2026-10-07"
        }
    },


    # ========================================================
    # MASSEY UNIVERSITY
    # ========================================================

    "Massey University": {

        "Master of Information Sciences": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1.5 years",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Information Sciences",
                    "Computer Science",
                    "Information Technology",
                    "Related field"
                ],

                "academic_requirement":
                    "B- average in qualifying 300-level majoring courses",

                "minimum_gpa": None,

                "minimum_grade": "B-",

                "prerequisites":
                    "Relevant undergraduate preparation"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "Professional pathway with project or research pathway with thesis",

            "source":
                "Official Massey University programme information",

            "last_verified":
                "2026-10-07"
        }
    },


    # ========================================================
    # LINCOLN UNIVERSITY
    # ========================================================

    "Lincoln University": {

        "Master of Applied Computing": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1.5 years",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Relevant bachelor's degree"
                ],

                "academic_requirement":
                    "B average or better in 300-level and final-year courses",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant academic background"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "180-credit applied computing master's programme",

            "source":
                "Official Lincoln University programme information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Artificial Intelligence for Land Use": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "1 year",

            "credits": 180,

            "intakes": ["February"],

            "eligibility": {

                "degree_background": [
                    "Relevant bachelor's degree"
                ],

                "academic_requirement":
                    "B average or better in 300-level and final-year courses",

                "minimum_gpa": None,

                "minimum_grade": "B",

                "prerequisites":
                    "Relevant academic preparation"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "140 credits coursework + 40-credit industry project/dissertation",

            "source":
                "Official Lincoln University programme information",

            "last_verified":
                "2026-10-07"
        }
    },


    # ========================================================
    # UNITEC INSTITUTE OF TECHNOLOGY
    # ========================================================

    "Unitec Institute of Technology": {

        "Master of Applied Technologies - Computing": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "18 months",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Computing",
                    "Information Technology",
                    "Similar discipline"
                ],

                "academic_requirement":
                    "B- or higher average in Level 7 courses",

                "minimum_gpa": None,

                "minimum_grade": "B-",

                "prerequisites":
                    "Recognised bachelor's degree in the same or similar discipline"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "specialisations": [
                "Data Analytics and Intelligence",
                "Cybersecurity and Networking",
                "Software Development"
            ],

            "programme_structure":
                "180-credit applied technologies master's programme",

            "source":
                "Official Unitec Institute of Technology programme information",

            "last_verified":
                "2026-10-07"
        }
    },


    # ========================================================
    # AUT - SCHOOL OF EDUCATION
    # ========================================================

    "Auckland University of Technology": {

        "Master of Education": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "Programme-specific",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Education",
                    "Teaching",
                    "Related field"
                ],

                "academic_requirement":
                    "Relevant bachelor's degree and programme-specific requirements",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "Relevant education/teaching background"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "180-credit postgraduate education qualification",

            "source":
                "Official AUT School of Education information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Education Practice": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "Programme-specific",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Education",
                    "Teaching",
                    "Related field"
                ],

                "academic_requirement":
                    "Relevant bachelor's degree and programme-specific requirements",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "Relevant education practice background"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "180-credit education practice qualification",

            "source":
                "Official AUT School of Education information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Educational Leadership": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "Programme-specific",

            "credits": 180,

            "intakes": ["February", "July"],

            "eligibility": {

                "degree_background": [
                    "Education",
                    "Teaching",
                    "Related field"
                ],

                "academic_requirement":
                    "Relevant bachelor's degree and programme-specific requirements",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "Relevant education or leadership background"
            },

            "english": {

                "IELTS": 6.5,

                "minimum_band": 6.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": False
            },

            "programme_structure":
                "180-credit education leadership programme",

            "source":
                "Official AUT School of Education information",

            "last_verified":
                "2026-10-07"
        },


        "Master of Teaching and Learning": {

            "status": "Active",

            "qualification_level": 9,

            "duration": "Programme-specific",

            "credits": 180,

            "intakes": ["February"],

            "eligibility": {

                "degree_background": [
                    "Bachelor's degree",
                    "Relevant subject background"
                ],

                "academic_requirement":
                    "Bachelor's degree plus selection and professional requirements",

                "minimum_gpa": None,

                "minimum_grade": None,

                "prerequisites":
                    "Teaching suitability, selection and professional requirements"
            },

            "english": {

                "IELTS": 7.0,

                "minimum_band": 7.0,

                "other_tests": []
            },

            "gre": {

                "required": False
            },

            "work_experience": {

                "required": False,

                "minimum_years": None
            },

            "research": {

                "required": True
            },

            "programme_structure":
                "Includes compulsory courses, research study and professional teaching practicum",

            "source":
                "Official AUT School of Education information",

            "last_verified":
                "2026-10-07"
        }
    }
}


# ============================================================
# 2. COMMON DISPLAY FUNCTION
# ============================================================

def show_options(options):

    for number, option in enumerate(options, 1):
        print(number, ".", option)


# ============================================================
# 3. CHOOSE UNIVERSITY
# ============================================================

def choose_university():

    university_list = list(universities.keys())

    print("\n========================================")
    print("       NEW ZEALAND UNIVERSITIES")
    print("========================================")

    show_options(university_list)

    while True:

        try:

            choice = int(input("\nChoose university number: "))

            if 1 <= choice <= len(university_list):

                return university_list[choice - 1]

            else:

                print("Invalid choice. Try again.")

        except ValueError:

            print("Please enter a number.")


# ============================================================
# 4. CHOOSE COURSE
# ============================================================

def choose_course(university):

    courses = list(universities[university].keys())

    print("\n========================================")
    print("          AVAILABLE PROGRAMMES")
    print("========================================")

    show_options(courses)

    while True:

        try:

            choice = int(input("\nChoose programme number: "))

            if 1 <= choice <= len(courses):

                return courses[choice - 1]

            else:

                print("Invalid choice. Try again.")

        except ValueError:

            print("Please enter a number.")


# ============================================================
# 5. SHOW PROGRAMME INFORMATION
# ============================================================

def show_programme_details(university, course):

    requirements = universities[university][course]

    print("\n========================================")
    print("       PROGRAMME INFORMATION")
    print("========================================")

    print("\nUniversity:")
    print(university)

    print("\nProgramme:")
    print(course)

    print("\nStatus:")
    print(requirements["status"])

    print("\nQualification Level:")
    print(requirements["qualification_level"])

    print("\nDuration:")
    print(requirements["duration"])

    print("\nCredits:")
    print(requirements["credits"])

    print("\nIntakes:")
    print(", ".join(requirements["intakes"]))

    print("\n----------------------------------------")
    print("ELIGIBILITY")
    print("----------------------------------------")

    eligibility = requirements["eligibility"]

    print("\nDegree Background:")

    for degree in eligibility["degree_background"]:

        print("-", degree)

    print("\nAcademic Requirement:")
    print(eligibility["academic_requirement"])

    print("\nMinimum GPA:")
    print(eligibility["minimum_gpa"])

    print("\nMinimum Grade:")
    print(eligibility["minimum_grade"])

    print("\nPrerequisites:")
    print(eligibility["prerequisites"])

    print("\n----------------------------------------")
    print("ENGLISH REQUIREMENT")
    print("----------------------------------------")

    english = requirements["english"]

    print("IELTS Overall:", english["IELTS"])

    print("Minimum Band:", english["minimum_band"])

    print("Other Tests:")

    for test in english["other_tests"]:

        print("-", test)

    print("\n----------------------------------------")
    print("OTHER REQUIREMENTS")
    print("----------------------------------------")

    print("\nGRE Required:")
    print(requirements["gre"]["required"])

    print("\nWork Experience Required:")
    print(requirements["work_experience"]["required"])

    if requirements["work_experience"]["required"]:

        print(
            "Minimum Work Experience:",
            requirements["work_experience"]["minimum_years"],
            "years"
        )

    print("\nResearch Required:")
    print(requirements["research"]["required"])

    if "specialisations" in requirements:

        print("\nSpecialisations:")

        for specialisation in requirements["specialisations"]:

            print("-", specialisation)

    print("\nProgramme Structure:")
    print(requirements["programme_structure"])

    print("\nSource:")
    print(requirements["source"])

    print("\nLast Verified:")
    print(requirements["last_verified"])


# ============================================================
# 6. GET STUDENT PROFILE
# ============================================================

def get_student_profile():

    print("\n========================================")
    print("          STUDENT PROFILE")
    print("========================================")

    cgpa = float(input("Enter your CGPA: "))

    degree = input("Enter your bachelor's degree: ")

    ielts = float(input("Enter IELTS overall score: "))

    lowest_band = float(
        input("Enter your lowest IELTS band: ")
    )

    total_arrears = int(
        input("Enter total number of arrears/backlogs: ")
    )

    recent_arrears = int(
        input("Enter arrears in the last 2 years: ")
    )

    active_backlogs = int(
        input("Enter current active backlogs: ")
    )

    projects = int(
        input("Enter number of relevant projects: ")
    )

    internships = int(
        input("Enter number of internships: ")
    )

    research = int(
        input("Enter number of research experiences: ")
    )

    work_experience = float(
        input("Enter work experience in years: ")
    )

    student = {

        "cgpa": cgpa,

        "degree": degree,

        "ielts": ielts,

        "ielts_lowest_band": lowest_band,

        "total_arrears": total_arrears,

        "recent_arrears": recent_arrears,

        "active_backlogs": active_backlogs,

        "projects": projects,

        "internships": internships,

        "research": research,

        "work_experience": work_experience
    }

    return student


# ============================================================
# 7. CHECK ENGLISH
# ============================================================

def check_english(student, requirements):

    required_ielts = requirements["english"]["IELTS"]

    minimum_band = requirements["english"]["minimum_band"]

    print("\n========================================")
    print("ENGLISH REQUIREMENT CHECK")
    print("========================================")

    print("Required IELTS:", required_ielts)

    print("Student IELTS:", student["ielts"])

    print("Required minimum band:", minimum_band)

    print("Student lowest band:", student["ielts_lowest_band"])

    if student["ielts"] >= required_ielts:

        print("\nIELTS overall: MEETS")

    else:

        print("\nIELTS overall: DOES NOT MEET")

    if student["ielts_lowest_band"] >= minimum_band:

        print("Minimum band: MEETS")

    else:

        print("Minimum band: DOES NOT MEET")


# ============================================================
# 8. CHECK ACADEMIC PROFILE
# ============================================================

def check_academic(student, requirements):

    print("\n========================================")
    print("ACADEMIC PROFILE")
    print("========================================")

    print("Student CGPA:", student["cgpa"])

    print(
        "Academic requirement:",
        requirements["eligibility"]["academic_requirement"]
    )

    minimum_gpa = requirements["eligibility"]["minimum_gpa"]

    if minimum_gpa is not None:

        if student["cgpa"] >= minimum_gpa:

            print("Academic GPA: MEETS minimum stated GPA")

        else:

            print("Academic GPA: BELOW minimum stated GPA")

    else:

        print(
            "Exact GPA comparison cannot be calculated yet."
        )

        print(
            "The programme uses a grade/subject-specific requirement."
        )


# ============================================================
# 9. CHECK DEGREE BACKGROUND
# ============================================================

def check_degree(student, requirements):

    print("\n========================================")
    print("DEGREE BACKGROUND")
    print("========================================")

    print("Student degree:")
    print(student["degree"])

    print("\nExpected backgrounds:")

    for degree in requirements["eligibility"]["degree_background"]:

        print("-", degree)

    print(
        "\nDetailed degree matching will be added "
        "in a later version."
    )


# ============================================================
# 10. CHECK WORK EXPERIENCE
# ============================================================

def check_work_experience(student, requirements):

    print("\n========================================")
    print("WORK EXPERIENCE")
    print("========================================")

    required = requirements["work_experience"]["required"]

    minimum_years = requirements["work_experience"]["minimum_years"]

    student_experience = student["work_experience"]

    print("Student experience:", student_experience, "years")

    if required:

        print("Required experience:", minimum_years, "years")

        if minimum_years is not None:

            if student_experience >= minimum_years:

                print("Work experience: MEETS requirement")

            else:

                print("Work experience: DOES NOT MEET requirement")

        else:

            print(
                "Experience is required, but exact minimum "
                "needs programme-specific verification."
            )

    else:

        print("Work experience: NOT REQUIRED")


# ============================================================
# 11. CHECK BACKLOG PROFILE
# ============================================================

def check_backlogs(student):

    print("\n========================================")
    print("BACKLOG / ARREAR PROFILE")
    print("========================================")

    print(
        "Total arrears:",
        student["total_arrears"]
    )

    print(
        "Arrears in last 2 years:",
        student["recent_arrears"]
    )

    print(
        "Active backlogs:",
        student["active_backlogs"]
    )

    if student["active_backlogs"] == 0:

        print("\nActive backlogs: GOOD")

    else:

        print(
            "\nActive backlogs: NEEDS ATTENTION"
        )

    if student["recent_arrears"] == 0:

        print(
            "Recent arrears: GOOD"
        )

    else:

        print(
            "Recent arrears: NEEDS INVESTIGATION"
        )

    print(
        "\nNOTE: These are profile risk indicators."
    )

    print(
        "They are NOT universal New Zealand university rules."
    )


# ============================================================
# 12. CHECK PROFILE FACTORS
# ============================================================

def analyse_profile_factors(student):

    print("\n========================================")
    print("PROFILE FACTORS")
    print("========================================")

    print(
        "Relevant projects:",
        student["projects"]
    )

    print(
        "Internships:",
        student["internships"]
    )

    print(
        "Research experiences:",
        student["research"]
    )

    print(
        "Work experience:",
        student["work_experience"],
        "years"
    )

    print("\nThese factors may strengthen an application.")

    print(
        "They are not automatically official admission requirements."
    )


# ============================================================
# 13. COMPLETE PROFILE ANALYSIS
# ============================================================

def analyze_profile(student, requirements):

    print("\n\n========================================")
    print("          PROFILE ANALYSIS")
    print("========================================")

    check_academic(
        student,
        requirements
    )

    check_degree(
        student,
        requirements
    )

    check_english(
        student,
        requirements
    )

    check_work_experience(
        student,
        requirements
    )

    check_backlogs(
        student
    )

    analyse_profile_factors(
        student
    )


# ============================================================
# 14. MAIN FUNCTION
# ============================================================

def main():

    print("\n")
    print("==============================================")
    print("   NEW ZEALAND UNIVERSITY ADMISSION SYSTEM")
    print("==============================================")

    print("\nPhase 1")
    print("University Data + Requirement Checker")

    university = choose_university()

    course = choose_course(
        university
    )

    show_programme_details(
        university,
        course
    )

    student = get_student_profile()

    requirements = universities[
        university
    ][
        course
    ]

    analyze_profile(
        student,
        requirements
    )

    print("\n========================================")
    print("             ANALYSIS COMPLETE")
    print("========================================")

    print("\nSelected University:")
    print(university)

    print("\nSelected Programme:")
    print(course)

    print("\nThank you for using the system!")


# ============================================================
# 15. RUN PROGRAM
# ============================================================

main()