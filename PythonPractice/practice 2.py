#students = {"name":"Prajan","age":20}
#students.items()
#print(students.items())
#print(students.keys())
#print(students.values())
cars = {"s1":{"name": "audi"},"s2":{"name":"bmw"}}
print(cars["s1"]["name"])
cars["s3"] = {"name":"ferrari" }
print(cars["s3"])
print(cars)
cars["s1"]["name"] = "toyota"
print(cars)
print(cars["s3"]["name"])