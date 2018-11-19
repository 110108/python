# Repeat forever
# Ask "Enter 1 to convert Fahrenheit to Celsius, 2 to convert Celsius to Fahrenheit, or Q to Quit: "
# if choice = 1
# "What Fahrenheit temperature would you like to convert? "
# fahrenheitTemp - 32 * 5 / 9
# "That temperature in Celsius is ____"
# elif choice = 2
# "What Celsius temperature would you like to convert? "
# celsiusTemp * 9 / 5 + 32
# "That temperature in Fahrenheit is ____"
# else
# "PLEASE ENTER EITHER 1, 2, OR Q"
import random

run=True

while run:
    In=input("Enter 1 to convert Fahrenheit to Celsius, 2 to convert Celsius to Fahrenheit, or Q to Quit: ")
    if(In=="Q" or In=="q"):
        run = False
        continue
    if(In == "1"):
        ftemp=input("What Fahrenheit temperature would you like to convert? ")
        ftemp=int(ftemp)
        fperm=((ftemp-32)*5/9)
        fperm=str(fperm)
        print("That temperature in Celsius is "+(fperm))
    if(In == "2"):
        ctemp=input("What Celsius temperature would you like to convert? ")
        ctemp=int(ctemp)
        cperm=(ctemp * 9 / 5 + 32)
        cperm=str(cperm)
        print("That temperature in Fahrenheit is "+(cperm))
    else:
        print("PLEASE ENTER EITHER 1, 2, OR Q")
print("exot")