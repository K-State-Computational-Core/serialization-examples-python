class Pet:
    
    def __init__(self, name, age, breed):
        self.__name = name
        self.__age = age
        self.__breed = breed
        
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
    def breed(self):
        return self.__breed
    
    @breed.setter
    def breed(self, breed):
        self.__breed = breed

    def __str__(self):
        return "Pet\nName = {}\nAge = {}\nBreed = {}".format(self.name, self.age, self.breed)
