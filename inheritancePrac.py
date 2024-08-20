class Pet:
    def __init__(self, name, age):
        self.name:int = name
        self.age:str = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old. " )

class Cat(Pet):
    def __init__(self, name, age, colour):
         super().__init__(name, age)
         self.colour = colour

    def show(self):
         print(f"I am {self.name} and I am {self.age} years old, and I am {self.colour}. ")

    def speak(self):
        print("Meow")

class Dog(Pet):
        def speak(self):
            print("Bark")


p = Pet("Tim", 19)
p.show()

c = Cat("Bill", 34, "Orange")
c.show()

d = Dog("Jill", 25)
d.show()



c.speak()
d.speak()
