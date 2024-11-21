from Coin import Coin
from Dice.Dice import D20
from Dice.Dice import D4
from Dice.Dice import D6
from Dice.Dice import Dice

class Main(Dice):
    diceBag = [D6(), Coin(), D20(), D4()]
    for dice in diceBag:
        print("Lançons le dé D" + str(Dice.NbSides) + "\t:", dice.roll())

# myD6 = Dice()
# myCoin = Dice(2)
#
# print(myD6.NbSides)
# print(myCoin.NbSides)
#
# for i in range(10):
#     print(f"D{MYd6})