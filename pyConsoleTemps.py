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
    if(In==81 or In==113):
        continue
    if(In is 1):
        ftemp=input("What Fahrenheit temperature would you like to convert? ")
        print("That temperature in Celsius is "+((ftemp-32)*5/9))
