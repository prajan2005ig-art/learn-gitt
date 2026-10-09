#def greet(n):
    #print("Hello World",n)

#greet("c")
#greet("c")
#greet('v')

#def add(a,b):
    #return a+b
#result = add(3,5)
#print(result)
students = {}

# ➕ Add Student
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    students[sid] = {"name": name, "age": age}
    print("✅ Student added successfully!\n")


# 👀 View Students
def view_students():
    if not students:
        print("No students found.\n")
        return

    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}")
    print()


# 🔍 Search Student
def search_student():
    sid = input("Enter Student ID to search: ")

    if sid in students:
        print("Found:", students[sid], "\n")
    else:
        print("❌ Student not found\n")


# ✏️ Update Student
def update_student():
    sid = input("Enter Student ID to update: ")

    if sid in students:
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))

        students[sid]["name"] = name
        students[sid]["age"] = age

        print("✅ Student updated!\n")
    else:
        print("❌ Student not found\n")


# ❌ Delete Student
def delete_student():
    sid = input("Enter Student ID to delete: ")

    if sid in students:
        del students[sid]
        print("✅ Student deleted!\n")
    else:
        print("❌ Student not found\n")


# 🧭 Menu System
def menu():
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


# ▶️ Main Program
while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("👋 Exiting program...")
        break

    else:
        print("❌ Invalid choice\n")