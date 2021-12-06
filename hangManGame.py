
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:11:56 2021

@author: Tas
"""
import random
from time import sleep

#------------------Hangman-----------------------------------------------------
hangMan = [
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
"""]
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
words = ["SUBWAY", "LUCKY","PIZZA", "APPLE", "ORACLE", "MIMO", "TESLA", "PLAYSTATION", "WAVE", "QUEUE", "UNKNOWN", "TYPICAL", "RICE", "RENTAL", "SWEDEN", "PAKISTAN"]
word = random.choice(words)
positiveSaying = ["Well done!", "Awesome!", "You Legend!"]
total = maxWrong = len(hangMan) - 1
soFar = ("-") * len(word)
usedAlphabets = []
wrong = 0
#------------------------------------------------------------------------------
# -----------------------User Input Func---------------------------------------
def getChoice():
    while True:
        guess = input("Guess a letter: ").upper()
        if guess.isalpha() is True:
            return guess
            break
        else:
            print("Please input only alphabet") 
            continue
         
#------------------------------------------------------------------------------
           

print("\n\t \t  Welcome to Hangman!\n")

input("Press Enter to START: ")

while wrong < maxWrong and soFar != word:
    
    print()
    print(hangMan[wrong])

    print("Word so far: ", soFar)
    print("Letters used: ", usedAlphabets)
    print("Maximum wrong answer",total)
    guess = getChoice()
    while guess in usedAlphabets:
        print("Try again... You've already used this letter")
        guess = getChoice()
        #guess = input("Guess a letter: ").upper()
        sleep(1)
    print()
    usedAlphabets.append(guess)
    
    if guess in word:
        print(random.choice(positiveSaying))

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += soFar[i]
        soFar = new 
    else:
        print("INCORRECT! Try again!")
        wrong += 1
        total = maxWrong - wrong
        
print("Calculating result...")
sleep(2)
if wrong == maxWrong:
    print("UNLUCKY! Better luck next time!")
    print(hangMan[-1])
    print ("Correct word was: ",word)

else:
    print("WINNER! Congratulations!")


print("\n\n")
input("Press Enter to Leave: ")
