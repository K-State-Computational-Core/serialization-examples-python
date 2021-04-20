from Person import Person
from Pet import Pet
import json
import sys


class LoadJson:
    
    @staticmethod
    def main(args):
        with open("person.json") as file:
            person_dict = json.load(file)

        person = Person(
            person_dict['name'],
            person_dict['age'],
            Pet(
                person_dict['pet']['name'],
                person_dict['pet']['age'],
                person_dict['pet']['breed']))
        
        print("Loading person:")
        print(person)


if __name__ == "__main__":
    LoadJson.main(sys.argv)
