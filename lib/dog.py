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
    def __init__(self, name="", breed=""):
        self._name = name
        self._breed = breed
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be a string between 1 and 25 characters.")


    @property
    def breed(self):
        return self._breed
    @breed.setter
    def breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in the list of approved breeds.")
            
        else:
            self._breed = breed




fido = Dog()  
zero = Dog(name="Zero", breed="Corgi")  

    