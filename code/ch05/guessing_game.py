import random

random.seed(7)  # remove this line to get a different number each game
secret = random.randint(1, 100)
tries = 0

print("I'm thinking of a number from 1 to 100.")
while True:
    guess = int(input("Your guess: "))
    tries += 1
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print(f"Correct! You found it in {tries} tries.")
        break
