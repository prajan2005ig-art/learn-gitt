students = {}

def load_data():
    file = open("students.txt","r")
    for line in file:
        line = line.strip()

        if not line:
            continue

        data = line.split(",")

        sid = int(data[0])
        name = data[1]
        age = int(data[2])
        cgpa = float(data[3])

        students[sid] = {"name" : name,"age" : age,"cgpa" : cgpa}
    file.close()

def save_data():
    file = open("students.txt","w")
    for sid,info in students.items():
        file.write(f"{sid},{info['name']},{info['age']},{info['cgpa']}\n")
    file.close()
    print("Student saved")

def valid_id():
    while True:
        try:
            return int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID")

def valid_age():
    while True:
        try:
            return int(input("Enter Student Age: "))
        except ValueError:
            print("Invalid Age")

def valid_cgpa():
    while True:
        try:
            return float(input("Enter CGPA: "))
        except ValueError:
            print("Invalid CGPA")

def valid_choice():
    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Choice")

def define_details():
        sid = valid_id()

        if sid in students:
            print("Student ID already exists")
            return

        name = input("enter the name")
        age = valid_age()
        cgpa = valid_cgpa()

        students[sid] = {"name" : name,"age" : age,"cgpa" : cgpa}
        save_data()
        print("Student added!")

def view_students():
    if not students:
        print("Student list is empty")
        return

    for sid,info in students.items():
        print("Student ID:",sid)
        print("Name:",info["name"])
        print("Age:",info["age"])
        print("CGPA:",info["cgpa"])

def update_students():
    sid = int(input("Enter Student ID: "))

    if sid in students:
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        cgpa = float(input("Enter CGPA: "))
        students[sid]["name"] = name
        students[sid]["age"] = age
        students[sid]["cgpa"] = cgpa
        save_data()

    else :
        print("std id not found")
        return

def del_students():
    sid = int(input("Enter Student ID: "))
    if sid in students:
        del students[sid]
        save_data()
        print("Student deleted")
        return

def exit_program():
    print("Exit")
    exit()

def menu():
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Students")
    print("4. Delete Students")
    print("5. Exit")

load_data()

while True:
    menu()
    choice = valid_choice()

    if choice == 1:
        define_details()

    elif choice == 2:
        view_students()

    elif choice == 3:
        update_students()

    elif choice == 4:
        exit_program()

    else:
        print("Invalid Choice")