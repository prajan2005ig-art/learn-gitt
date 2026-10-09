#file = open("cars.txt","r+")
#file.write("hello world\n,hi\n,ooh\n ")
#file.close()
with open("file.txt","a") as file:
    print(file.write("open") )
