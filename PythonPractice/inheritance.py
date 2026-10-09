class animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def talk(self):
        print(f"{self.name} cannot talk ")

    def speak(self):
        print(f"{self.name} can speak")

    def run(self):
        print(f"{self.name} can run")

class dog(animal):
    pass

class cat(animal):
    pass

DOG = dog("dog")
CAT = cat("cat")


DOG.talk()
CAT.speak()
print(DOG.name)
print(CAT.name)
print(DOG.is_alive)
DOG.run()
#example for how inheritance works