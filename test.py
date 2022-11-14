
from abc import ABC, abstractmathod

class Human(ABC):

    @abstractmathhod
    def makan(self):
        print("Manusia itu suka makan")

class Hero(Human):
    pass

person = Hero()
person.makan()


  