class Person:
    
    def __init__(self, name, age, pet):
        self.__name = name
        self.__age = age
        self.__pet = pet
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
        
    @property
    def pet(self):
        return self.__pet
    
    @pet.setter
    def pet(self, pet):
        self.__pet = pet
        
    def __str__(self):
        return "Person\nName = {}\nAge = {}\n{}".format(self.name, self.age, self.pet)
