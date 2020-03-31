import random

# Defining guessing Function
def guessing():
    n = random.randint(1,10)
    chances = 0
    guess = int(input("Guess the number: "))
    while chances<5:
        if n == guess:
            print("you guessed it right")
            break
        elif n < guess:
            print("Number too high, guess the number lower than ", guess)
        else:
            print("number too low, guess the number higher than ", guess)
        guess = int(input("Guess again: "))
        chances += 1

    if not chances < 5:
        print("you lost")

# Run Guessing Function
if __name__ == "__main__":
    guessing()