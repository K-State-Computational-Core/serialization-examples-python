from Person import Person
from Pet import Pet
import xml.etree.ElementTree as ET
import sys


class LoadXml:
    
    @staticmethod
    def main(args):
        
        xml_tree = ET.parse("person.xml")
        person_elem = xml_tree.getroot()
        
        for child in person_elem:
            if child.tag == "name":
                name = child.text
            if child.tag == "age":
                age = child.text
            if child.tag == "pet":
                for subchild in child:
                    if subchild.tag == "name":
                        pet_name = subchild.text
                    if subchild.tag == "age":
                        pet_age = subchild.text
                    if subchild.tag == "breed":
                        pet_breed =subchild.text

        person = Person(name, age, Pet(pet_name, pet_age, pet_breed))
        
        print("Loading person:")
        print(person)


if __name__ == "__main__":
    LoadXml.main(sys.argv)
