from Person import Person
from Pet import Pet
import pickle
import sys


class SaveBinary:
    
    @staticmethod
    def main(args):
        person = Person("Willie Wildcat", 42, Pet("Reggie", 4, "Shorkie"))
        print("Saving person:")
        print(person)
        
        with open("person.p", "wb") as file:
            pickle.dump(person, file)


if __name__ == "__main__":
    SaveBinary.main(sys.argv)
