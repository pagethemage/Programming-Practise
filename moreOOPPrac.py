class Animal:
    def __init__(self, name:str, species:str):
        self.name:str = name
        self.species:str = species

    def make_sound(self):
        return ("Noooooooiise! (I dont know, its a generic sound. )")
    
 
    @property
    def name(self):
        return self._name

    @name.setter ##Remember, method has to share name with attribute it sets
    def name(self, x):
        self._name = x

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, x):
        self._species = x
    
    def get_species(self):
        return self.species
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return (f"My name is: {self.name} and I am of {self.pecies} species.")
    

    
    

class Dog(Animal):
    def __init__(self, name:str, species:str, breed:str):
        super().__init__(name, species)
        self.breed:str = breed

    def make_sound(self):
        return ("woof!")
    
    def __str__(self):
        return (f"My name is {self().get_name()} and I am a {self().species()} of type {self.breed}")
    

class Cat(Animal):
    def __init(self, name, colour):
        super().__init__(name, species="Dog")


d1 = Dog("Rocko", "Dog", "Dachshund")
    


## Properties: Identical in purpose to setter function, however:
    ## Property method name MUST MATCH attribute they re-define
    ## Properties are called by redefining variable name of instance of object
    ## ie. dog1.name = Rocko
    ## if there is a property called name(self, new_name) in class Dog,
    ## Dog's name will be set to Rocko



## TODO:
    ## Finish Dog class
    ## Finish Cat class
    ## Finish petlist class to contain objects
        ## > Allow iteration through objects
        ## > Give them methods, use PatientRecordSystem as inspiration 
