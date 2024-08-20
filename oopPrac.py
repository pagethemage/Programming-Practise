class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def getAge(self):
        return self.age



    def getName(self):
        return self.name

    # def bark(self):
    #     print("bark!")

    def add_one(self, x):
        return x + 1

petList:list = []


class Cat:
    def meow(self):
        print("Meow!")

d = Dog("Tim", 40)
print(f"{d.getName()} {d.getAge()} ")
d2 = Dog("Bill", 3)
print(d2.getName())


print(d.add_one(5))




# h = Dog()
# x = Dog()
# a = Cat()
# b = Cat()
# c = Cat()

# petList.append(d)
# petList.append(h)
# petList.append(x)
# petList.append(a)
# petList.append(b)
# petList.append(c)

# for z in petList:
#     if isinstance (z, Dog):
#         z.bark()
#     elif isinstance (z, Cat):
#         z.meow()



# d.bark()
# print(type(d))


def main():
    return


## When you will be declaring instance of a method, it has to pass self as first argument in method declaration
## eg. def bark(self): in the dog class