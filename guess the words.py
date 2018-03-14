import random

words = ["Computer Science","History","English","Math"]

hint1 = ["Making game","America","good reads","Binomial"]

hint2 = ["Python","Franklin Roosevelt","Grammer","Calculater"]

number = random.randint(0,3)

secretword = words[number]

guess = ""

counter = 0

while True:
    print("Guess the secret word!")
    print("type 'hint1', hint2' or give up' for help.")
    guess = input() 

    if guess == secretword:
        print = input("you got it")
        break

    elif guess == "hint1":
        print( hint1[number] )

    elif guess == "hint2":
        print(hint2[number] )


    elif guess == "give up":
        print("The word was " + secretword)
        break 
