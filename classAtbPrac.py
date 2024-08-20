class Person:
    number_of_people = 0 ## Variables defined up here are set as class level variables, will apply to this class and every instance of it

    def __init__(self, name):
        self.__name:str = name
        Person.add_person()
        ## increments class level variable every time person object declared

    def get_name(self):
        return self.__name
    
    @classmethod
    def show_total_people(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1



p1 = Person("Tim")
p2 = Person("Jill")
print(Person.show_total_people())
# print(Person.number_of_people)
# print(p1.__name)