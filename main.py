from dice import Account, Dice
from random import randint

def intro():
    print("Welcome to Dice Simulator 5000!")
    name = input("\nPlease enter your name\n>> ")
    opening_balance = int(input("\nPlease enter your opening balance\n>> $"))
    account = Account(name, opening_balance)
    """
        account object is set above.
    """
    return account


def main(account):
    print("Hi " + account.name + ". Your balance is $" + str(account.balance))
    wager = int(input("\nHow much do to want to wager?\n>> $"))

    if wager > account.balance:
        print("\nYou don't have enough money to place that bet.")
    else:
        print("Ok. Your wager is $" + str(wager))
        i = input("\nYour first roll needs to be 7 or 11 to win.\nEnter 'Roll' to play or 'Quit' to exit.\n\n>> ")

        if i.lower() ==  "quit":
            raise SystemExit
        elif i.lower() == "roll":
            d1 = Dice()
            d1.roll()

            print("You rolled a " + str(d1.get_value()))

            """
                Checks the first dice to see if it is 7 or 11. If so the player wins their wager
                and go back to the beginning of the main method.
            """
            if d1.seven_or_eleven():
                account.winner(wager)
                print("Congratulations " + account.name + "! You won! Your balance is now $"
                        + str(account.balance) + ".\n")
                main(account)

            # Now we roll again. I simulated this by created a second dice object that keeps "rolling" until
            # it hits 7, 11, or the value of the original roll. Once one of those 3 is rolled the account is increased
            # or decreased depeding on the outcome. If the player still has money to play they are sent back to the beginning
            # of the main method.
            else:
                print("You need to roll " + str(d1.get_value()) + " again to win. If you roll a 7 or 11 you lose.")
                d2 = Dice()
                d2.roll()
                print("You rolled a " + str(d2.get_value()) + ".")

                while d2.seven_or_eleven() == False or d2.get_value() != d1:
                    d2.roll()
                    print("You rolled a " + str(d2.get_value()) + ".")


                    if d2.get_value() == d1.get_value():
                        account.winner(wager)
                        print("Congratulations " + account.name + "! You won! Your balance is now $" + str(account.balance) + ".\n")
                        main(account)

                    elif d2.seven_or_eleven():
                        account.loser(wager)
                        print("Sorry " + account.name + ". You lost. Your balance is now $" + str(account.balance) + ".")

                        if (account.broke()):
                            print("Your account balance is $" + str(account.balance) + ".  You'll have to get more money.")
                            raise SystemExit
                        else:
                            main(account)
        else:
            print("You didn't enter a correct input.\n")

main(intro())
