# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:12:15 2020

@author: James.Thomas
"""
# Hangman
# 
import random

mylist = list()
guess_num = int()
bad_guess_num = int()
wordlength = int()
returnedword = ' '
word = list()
result = [' ', ' ', ' ', ' ', ' ', ' ']
found = bool()
one = ' '
two = ' '
three = ' '
four = ' '
five = ' '
six = ' '

guess_num = 0
bad_guess_num = 0





def display_man(bad_guess_num):
    
    if bad_guess_num == 0:
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('------------------')
        print('|                |')
        print('------------------')
        print(result)

    if bad_guess_num == 1:
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(0 0)|')
        print('|       |  -  |')
        print('|        -----')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('------------------')
        print('|                |')
        print('------------------')
        print(result)

    if bad_guess_num == 2:
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(0 0)|')
        print('|       |  -  |')
        print('|        -----')
        print('|        /   \ ')
        print('|        |   |')
        print('|        |   |')
        print('|        -----')
        print('|')
        print('|')
        print('------------------')
        print('|                |')
        print('------------------')
     
    if bad_guess_num == 3:
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(0 0)|')
        print('|       |  -  |')
        print('|        -----')
        print('|        /   \________')
        print('|        |   |--------')
        print('|        |   |')
        print('|        ----- ')
        print('|')
        print('|')
        print('|')
        print('------------------')
        print('|                |')
        print('------------------')

    if bad_guess_num == 4:
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(0 0)|')
        print('|       |  -  |')
        print('|        -----')
        print('|  ______/   \________')
        print('|  ------|   |--------')
        print('|        |   |')
        print('|        -----  ')
        print('|')
        print('|')
        print('|')
        print('------------------')
        print('|                |')
        print('------------------')    

    if bad_guess_num == 5:
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(0 0)|')
        print('|       |  -  |')
        print('|        -----')
        print('|  ______/   \________')
        print('|  ------|   |--------')
        print('|        |   |')
        print('|        ---\ \         ')
        print('|            \ \     ')
        print('|             \ \__       ')
        print('|              |___|')
        print('------------------')
        print('|                |')
        print('------------------')

    if bad_guess_num == 6:
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(0 0)|')
        print('|       |  -  |')
        print('|        -----')
        print('|  ______/   \________')
        print('|  ------|   |--------')
        print('|        |   |')
        print('|        / /\ \         ')
        print('|       / /  \ \     ')
        print('|    __/ /    \ \__       ')
        print('|    |___|     |___|')
        print('------------------')
        print('|                |')
        print('------------------')


# Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def make_a_guess():
    global guess_num
    global bad_guess_num
    found = False    
    guess = input('Enter a letter to make a guess: ')
    guess = guess.upper()
    #print(global guess_num)
    print(guess)
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)
    print(six)
    print(result)
    
    if guess == one:
        result[0] = one 
        guess_num += 1  
    if guess == two :
        result[1] = two
        guess_num += 1  
    if guess == three :
        result[2] = three  
        guess_num += 1   
    if guess == four :
        result[3] = four
        guess_num += 1  
    if guess == five:
        result[4] = five
        guess_num += 1  
    if guess == six:
        result[5] = six
        guess_num += 1  
    else:
        bad_guess_num += 1

    return



#--------------------------------------------------------------------
#--------------------------------------------------------------------



print('Welcome to Hang Man!')

while True:

    
    if guess_num == 0:
        # Choose a word...
        mylist = ["APPLES", "ORANGE", "BANANA" ]
        returnedword = (random.choice(mylist))
        word = str(returnedword)
        wordlength = len(word)
        

        wordList = [letter for letter in word]
        one, two, three, four, five, six = wordList

    display_man(guess_num)
    make_a_guess()
   
     
    
    if found == True and wordlength == guess_num:
        print("You Win!")
        break
                   
            
    if  guess_num >= wordlength:
        print("Stretch his neck boys!")
        print(f'The word was: {returnedword}')
        print(word)
        break
          
            
