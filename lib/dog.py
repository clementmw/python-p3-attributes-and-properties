#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__ (self,name,breed):

        if 1 <= len(name) <=25:
            self.name = name
            print(name)
        else:
            print ("Name must be string between 1 and 25 characters.")
        
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")

bosco = Dog("sffgdvv","Pu")

   

    




        
