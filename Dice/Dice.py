from abc import ABC
from random import randint
class Dice(ABC):
    __nbSides:int

    def__init__ (self, nbSides:int = 6):
    self.__nbSides = max (nbSides = 2)

    def roll(self, parameter1: int) -> None :pass

    def get_nb_sides(self) -> int:
        return self.__nbSides

    def set_nb_sides(self, nbSides: int) -> None:
        self.__nbSides = max(nbSides, 1)

    def roll(self) -> int:
        return randint(1, self.__nbSides)

