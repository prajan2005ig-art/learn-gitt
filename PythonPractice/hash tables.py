students = {}

students["name"] = "jack"
students["age"] = 20

print(students)

if "name" in students:
    print("found")

del students["age"]
print(students)