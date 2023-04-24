import random

low = int(input("enter lower bound: "))
high = int(input("enter higher bound: "))

number = random.randint(low,high)

x = False
turns = 0
while(x==False):
    guess = int(input("enter a number :"))
    if guess==number:
        print("Congrats you guessed the number in "+ str(turns) + " turns. You have won!!!")
        x = True
    if guess>number:
        print("That's too high. Guess Again")
        turns += 1
    if guess<number:
        print("That's too low. Guess Again")
        turns += 1
