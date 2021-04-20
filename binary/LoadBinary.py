from Person import Person
from Pet import Pet
import pickle
import sys


class LoadBinary:
    
    @staticmethod
    def main(args):
        with open("person.p", "rb") as file:
            person = pickle.load(file)
        
        print("Loading person:")
        print(person)


if __name__ == "__main__":
    LoadBinary.main(sys.argv)
