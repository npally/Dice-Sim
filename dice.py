from random import randint
import time

class Dice(object):
    """
        blueprint for dice
    """
    def __init__(self):
        self.c = 0

    def roll(self):
        print("\nRolling\n...")
        for x in range(2):
            time.sleep(.5)
            print("...")
        x = randint(1, 6)
        y = randint(1, 6)
        self.c = x + y


    def seven_or_eleven(self):
        if self.c == 7 or self.c == 11:
            return True
        else:
            return False

    def get_value(self):
        return self.c



class Account(object):
    """
        blue print for account
    """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def winner(self, x):
        self.balance += x

    def loser(self, x):
        self.balance -= x

    def broke(self):
        if self.balance == 0:
            return True
        else:
            return False
