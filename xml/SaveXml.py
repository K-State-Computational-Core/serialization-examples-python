from Person import Person
from Pet import Pet
import xml.etree.ElementTree as ET
import sys


class SaveXml:
    
    @staticmethod
    def main(args):
        person = Person("Willie Wildcat", 42, Pet("Reggie", 4, "Shorkie"))
        print("Saving person:")
        print(person)
        
        person_elem = ET.Element("person")
        ET.SubElement(person_elem, "name").text = person.name
        ET.SubElement(person_elem, "age").text = str(person.age)
        pet_elem = ET.SubElement(person_elem, "pet")
        ET.SubElement(pet_elem, "name").text = person.pet.name
        ET.SubElement(pet_elem, "age").text = str(person.pet.age)
        ET.SubElement(pet_elem, "breed").text = person.pet.breed
        
        with open("person.xml", "w") as file:
            file.write(ET.tostring(person_elem, encoding="unicode"))


if __name__ == "__main__":
    SaveXml.main(sys.argv)
