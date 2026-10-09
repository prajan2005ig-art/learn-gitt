students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    # ADD STUDENT
    if choice == "1":
        sid = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        students[sid] = {"name": name, "age": age}
        print("Student added!")

    # VIEW ALL
    elif choice == "2":
        for sid, info in students.items():
            print(sid, "->", info)

    # SEARCH
    elif choice == "3":
        sid = input("Enter student ID to search: ")
        if sid in students:
            print(students[sid])
        else:
            print("Student not found")

    # DELETE
    elif choice == "4":
        sid = input("Enter student ID to delete: ")
        if sid in students:
            del students[sid]
            print("Deleted!")
        else:
            print("Student not found")

    # EXIT
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")