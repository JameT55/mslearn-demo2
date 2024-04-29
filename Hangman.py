# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:12:15 2020

@author: James.Thomas
Hangman game

"""


import random

#-----------------------------
# Working Storage
#-----------------------------
firstTime = bool(True)
good_guess_num = int(0)
bad_guess_num = int(0)
letter_found = bool()
wordList = str()
wordLength = int()
randomWord = str()
randomPhrase = str()
result = list()
trashTalkList = list()


one = str()
two = str()
three = str()
four = str()
five = str()
six = str()
seven = str()
eight = str()
nine = str()
ten = str()



#--------------------------------------
# Function: to display the graphic
#--------------------------------------

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
        print('|        /   \\ ')
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
        print('|        /   \\________')
        print('|        |   |--------')
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
        print('|  ______/   \\________')
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
        print('|  ______/   \\________')
        print('|  ------|   |--------')
        print('|        |   |')
        print('|        ---\\ \\      ')
        print('|            \\ \\    ')
        print('|             \\ \\__   ')
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
        print(f'|       |(X X)|          {randomPhrase}')
        print('|       |  -  |')
        print('|        -----')
        print('|  ______/   \\________')
        print('|  ------|   |--------')
        print('|        |   |')
        print('|        / /\\ \\     ')
        print('|       / /  \\ \\    ')
        print('|    __/ /    \\ \\__  ')
        print('|    |___|     |___|')
        print('|')
        print('|')
        print('----------------------')
        print('|                    |')
        print('----------------------')

#---------------------------------------
# Function: Make a Guess
#---------------------------------------
def make_a_guess():
    global good_guess_num
    global bad_guess_num
    global letter_found 
    letter_found = False

    guess = input('Enter a letter to make a guess: ')
    guess = guess.upper()
   

    if guess == one:
        result[0] = one 
        good_guess_num += 1  
        letter_found = True

    if guess == two :
        result[1] = two
        good_guess_num += 1 
        letter_found = True 

    if guess == three :
        result[2] = three  
        good_guess_num += 1   
        letter_found = True

    if guess == four :
        result[3] = four
        good_guess_num += 1  
        letter_found = True

    if guess == five:
        result[4] = five
        good_guess_num += 1  
        letter_found = True

    if guess == six:
        result[5] = six
        good_guess_num += 1  
        letter_found = True

    
    if guess == seven:
        result[6] = seven
        good_guess_num += 1  
        letter_found = True

    
    if guess == eight:
        result[7] = eight
        good_guess_num += 1  
        letter_found = True

        
    if guess == nine:
        result[8] = nine
        good_guess_num += 1  
        letter_found = True

        
    if guess == ten:
        result[9] = ten
        good_guess_num += 1  
        letter_found = True

    if letter_found == False:
        bad_guess_num += 1


    print(result)
    return


#--------------------------------------------------------------------
# Mainline logic
#--------------------------------------------------------------------


print('Welcome to Hang Man!')

while True:

    
    if firstTime == True:
        
        firstTime = False

        trashTalkList = ["Stretch his neck boys!", "Necktie party time!!", "Watch him jump!", "You should have chosen another letter", 
                         "You will pay for that!!", "Try again", "Another try?", "What?"]
        randomPhrase = (random.choice(trashTalkList))
        
                # Choose a word... 
        wordList = ["APPLE", "PEACH", "PEAR", "PLUM", "BANANA", "ORANGE", "TANGERINE"]
        randomWord = (random.choice(wordList))
        

        word = [letter for letter in randomWord]

        # Display the number of characters in the word on the screen
        wordLength = len(randomWord)
        if wordLength == 4:
            one, two, three, four = word
            result = [' ',' ', ' ', ' ']
        if wordLength == 5:
            one, two, three, four, five = word
            result = [' ',' ', ' ', ' ', ' ']
        if wordLength == 6:
            one, two, three, four, five, six = word
            result = [' ',' ', ' ', ' ', ' ', ' ']
        if wordLength == 7:
            one, two, three, four, five, six, seven = word
            result = [' ',' ', ' ', ' ', ' ', ' ', ' ']
        if wordLength == 8:
            one, two, three, four, five, six, seven, eight = word
            result = [' ',' ', ' ', ' ', ' ', ' ', ' ', ' ']    
        if wordLength == 9:
            one, two, three, four, five, six, seven, eight, nine = word
            result = [' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 
        if wordLength == 10:
            one, two, three, four, five, six, seven, eight, nine, ten = word
            result = [' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 

        display_man(bad_guess_num)

    make_a_guess()
    display_man(bad_guess_num)
     
    
    if wordLength == good_guess_num:
        print("You Win!")
        break
                   
            
    if  bad_guess_num >= 6:
        print(f'The word was: {randomWord}')
        break
          
            
