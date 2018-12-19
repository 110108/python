import random

ans=random.randint(1,100)
guesses=0
print("Im thinking of a number between 1 and 100.")
while True:
    user=input("\nGuess the number: ")

    try:
        user=int(user)
    except:
        print("\nEnter a number! ")
        continue

    if(user != ans):
        guesses=guesses+1
        if(user<ans):
            print("\nToo low")
        if(user>ans):
            print("\nToo high")
    if(user == ans):
        print("\nYou got it in "+str(guesses)+" guesses!")
        break