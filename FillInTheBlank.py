chances = 3

def question(question, answer):
    sc = input(question)
    while(sc != answer and chances > 0):
        chances-=1
        sc = input("You Only Have "+chances+" Chances left\n"+question)
    print("Correct")

question("What is 132 in 10 bit binary? ", "0010000100")
question("What is the name of the Computer Science teacher at bradley?","Mr. Riely")
question("The first letter of the alphabet is: ", "a")
question("_ + 2 = 3","1")
question("Computer Science classes are in room ____ at bradley", "B267")