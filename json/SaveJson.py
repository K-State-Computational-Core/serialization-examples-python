from Person import Person
from Pet import Pet
import json
import sys


class SaveJson:
    
    @staticmethod
    def main(args):
        person = Person("Willie Wildcat", 42, Pet("Reggie", 4, "Shorkie"))
        print("Saving person:")
        print(person)
        
        person_dict = dict()
        person_dict['name'] = person.name
        person_dict['age'] = person.age
        person_dict['pet'] = dict()
        person_dict['pet']['name'] = person.pet.name
        person_dict['pet']['age'] = person.pet.age
        person_dict['pet']['breed'] = person.pet.breed
        
        with open("person.json", "w") as file:
            json.dump(person_dict, file)


if __name__ == "__main__":
    SaveJson.main(sys.argv)
