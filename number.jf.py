import random
import time

number = random.randint(1,100)

guess = 0

counter = 0

while True:
    print("Guess my number 1 through 100")
    guess = int (input())

    
    if guess == number:
        print("YOu get it nice job")
        print("you took " + str(counter) + "guesses")
        break

    elif guess > number:
        print("to high")

    elif guess < number:
        print("to low")
