from abc import ABC, abstractmethod

class animal:
    @abstractmethod
    def eat(self):
        pass

class Mammal(animal):
    def eat(self):
        print("nom nom")