from random import randint
import time

# Create a rolling dice simulation
def intro():
    s = input("Welcome to Dice Simulator 5000!\nYour first roll needs to be 7 or 11 to win.\nEnter 'Roll' to play or 'Quit' to exit.\n\n>> " )

    if s.lower() == 'quit':
        leave_program()
    elif s.lower() == 'roll':
        game()
    else:
        print("Please enter a correct response.")
        intro()

def leave_program():
    raise SystemExit

def roll():
    a = randint(1, 6)
    b = randint(1, 6)
    print("\nRolling\n...")
    time.sleep(.5) # Pause program for 1.5 seconds
    print("...")
    time.sleep(.5)
    print("...")
    time.sleep(.5)
    print(f"Dice 1 is {a}")
    time.sleep(2)
    print(f"Dice 2 is {b}")
    time.sleep(3)
    return a, b

def game():
    t = roll()
    x = t[0]
    y = t[1]
    z = x + y
    if z == 7 or z == 11:
        print(f"Your roll is {z}. Congratulations, You win!!\n")
        time.sleep(2)
        return play_again()
    else:
        s = input(f"Your roll is {z}. You need to roll a {z} again to win. If you roll a 7 or 11 you lose.\n\nPress Enter to roll again.\n>> ")
        r = roll()
        a = r[0]
        b = r[1]
        c = a + b
        print(f'Your roll is {c}.\n')
        time.sleep(2)

        if c == z:
            print(f'Congratulations you win!!!\n')
            time.sleep(2)
            play_again()

        elif c == 11 or c ==7:
            print(f"You lose, try again\n")
            time.sleep(2)
            play_again()

        while c != z or c != 11 or c != 7:
            print(f"You need a {z} to win.\n")
            r1 = roll()
            a = r1[0]
            b = r1[1]
            c = a + b
            print(f'Your roll is {c}.\n')
            time.sleep(3)

            if c == z:
                print(f'Congratulations you win!!!\n')
                time.sleep(4)
                play_again()

            elif c == 11 or c ==7:
                print(f"You lose try again\n")
                time.sleep(2)
                play_again()

        else:
            leave_program()

def play_again():
    t = input("Would you like to play again? Enter 'Yes' or 'No'.\n>> ")
    if t.lower() == 'yes':
        intro()
    elif t.lower() == 'no':
        leave_program()
    else:
        print("Please enter a correct response.")
        play_again()

intro()
