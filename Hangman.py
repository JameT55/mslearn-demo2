# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:12:15 2020

@author: James.Thomas
new change
"""
# Hangman
# 
import random

myList = list()
guess_num = int()
bad_guess_num = int()
wordLength = int()
returnedWord = ' '
word = list()
result = list()
letter_found = bool()

guess_num = 0
bad_guess_num = 0
one = ' '
two = ' '
three = ' '
four = ' '
five = ' '
six = ' '
seven = ' '
eight = ' '
nine = ' '
ten = ' '






def display_man(bad_guess_num):
    
    if bad_guess_num == 0:
        print('-----------------')
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
        print('----------------------')
        print('|                    |')
        print('----------------------')
        print(result)

    if bad_guess_num == 1:
        print('-----------------')
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(- -)|')
        print('|       |  =  |')
        print('|        -----')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('----------------------')
        print('|                    |')
        print('----------------------')
        print(result)

    if bad_guess_num == 2:
        print('-----------------')
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(- 0)|')
        print('|       |  =  |')
        print('|        -----')
        print('|        /   \ ')
        print('|        |   |')
        print('|        |   |')
        print('|        -----')
        print('|')
        print('|')
        print('----------------------')
        print('|                    |')
        print('----------------------')
     
    if bad_guess_num == 3:
        print('-----------------')
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(0 0)|')
        print('|       |  =  |')
        print('|        -----')
        print('|        /   \________')
        print('|        |  w|--------')
        print('|        |   |')
        print('|        ----- ')
        print('|')
        print('|')
        print('|')
        print('----------------------')
        print('|                    |')
        print('----------------------')

    if bad_guess_num == 4:
        print('-----------------')
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(0 0)|')
        print('|       |  =  |')
        print('|        -----')
        print('|  ______/   \________')
        print('|  ------|   |--------')
        print('|        |   |')
        print('|        -----  ')
        print('|')
        print('|')
        print('|')
        print('----------------------')
        print('|                    |')
        print('----------------------')    

    if bad_guess_num == 5:
        print('-----------------')
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(O O)|')
        print('|       |  O  |')
        print('|        -----')
        print('|  ______/   \________')
        print('|  ------|   |--------')
        print('|        |   |')
        print('|        ---\ \         ')
        print('|            \ \     ')
        print('|             \ \__       ')
        print('|              |___|')
        print('----------------------')
        print('|                    |')
        print('----------------------')

    if bad_guess_num == 6:
        print('-----------------')
        print('-----------------')
        print('|          |')
        print('|          |')
        print('|        --|--')
        print('|       |(X X)|')
        print('|       |  -  |')
        print('|        -----')
        print('|  ______/   \________')
        print('|  ------|   |--------')
        print('|        |   |')
        print('|        / /\ \         ')
        print('|       / /  \ \     ')
        print('|    __/ /    \ \__       ')
        print('|    |___|     |___|')
        print('|')
        print('|')
        print('----------------------')
        print('|                    |')
        print('----------------------')


# Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def make_a_guess():
    global guess_num
    global bad_guess_num
    global letter_found 
    letter_found = False

    guess = input('Enter a letter to make a guess: ')
    guess = guess.upper()
   

    if guess == one:
        result[0] = one 
        guess_num += 1  
        letter_found = True

    if guess == two :
        result[1] = two
        guess_num += 1 
        letter_found = True 

    if guess == three :
        result[2] = three  
        guess_num += 1   
        letter_found = True

    if guess == four :
        result[3] = four
        guess_num += 1  
        letter_found = True

    if guess == five:
        result[4] = five
        guess_num += 1  
        letter_found = True

    if guess == six:
        result[5] = six
        guess_num += 1  
        letter_found = True

    
    if guess == seven:
        result[6] = seven
        guess_num += 1  
        letter_found = True

    
    if guess == eight:
        result[7] = eight
        guess_num += 1  
        letter_found = True

        
    if guess == nine:
        result[8] = nine
        guess_num += 1  
        letter_found = True

        
    if guess == ten:
        result[9] = ten
        guess_num += 1  
        letter_found = True

    if letter_found == False:
        bad_guess_num += 1


    print(result)
    return



#--------------------------------------------------------------------
#--------------------------------------------------------------------



print('Welcome to Hang Man!')

while True:

    
    if guess_num == 0:
        # Choose a word... 
        myList = ["APPLE", "PEACH", "PEAR", "PLUM", "BANANA", "ORANGE"]
        returnedWord = (random.choice(myList))
        word = str(returnedWord)
        wordLength = len(word)
        
        wordList = [letter for letter in word]

        if wordLength == 4:
            one, two, three, four = wordList
            result = [' ',' ', ' ', ' ']
        if wordLength == 5:
            one, two, three, four, five = wordList
            result = [' ',' ', ' ', ' ', ' ']
        if wordLength == 6:
            one, two, three, four, five, six = wordList
            result = [' ',' ', ' ', ' ', ' ', ' ']
        if wordLength == 7:
            one, two, three, four, five, six, seven = wordList
            result = [' ',' ', ' ', ' ', ' ', ' ', ' ']
        if wordLength == 8:
            one, two, three, four, five, six, seven, eight = wordList
            result = [' ',' ', ' ', ' ', ' ', ' ', ' ', ' ']    
        if wordLength == 9:
            one, two, three, four, five, six, seven, eight, nine = wordList
            result = [' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 
        if wordLength == 10:
            one, two, three, four, five, six, seven, eight, nine, ten = wordList
            result = [' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 

        display_man(bad_guess_num)

    make_a_guess()
    display_man(bad_guess_num)
     
    
    if wordLength == guess_num:
        print("You Win!")
        break
                   
            
    if  bad_guess_num >= 6:
        print("        Stretch his neck boys!")
        print(f'The word was: {returnedWord}')
        break
          
            
