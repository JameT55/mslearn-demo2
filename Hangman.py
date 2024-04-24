# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:12:15 2020

@author: James.Thomas
"""
# Hangman
# 
import random
guess_num = 1
returnedword = ' '
word = list(returnedword)
result = [' ', ' ', ' ', ' ', ' ', ' ']
found = bool()

game_on = True
marker = '2'
position = ' '
player1_turn = True






def display_man(guess_num):
    if guess_num == 1:
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

    if guess_num == 2:
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

    if guess_num == 3:
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
     
    if guess_num == 4:
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

    if guess_num == 5:
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

    if guess_num == 6:
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

    if guess_num == 7:
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
    found = False    
    guess = input('Enter a letter to make a guess: ')
    guess = guess.upper()
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
        found = True   
    if guess == two :
        result[1] = two
        found = True
    if guess == three :
        result[2] = three  
        found = True  
    if guess == four :
        result[3] = four
        found = True
    if guess == five:
        result[4] = five
        found = True
    if guess == six:
        result[5] = six
        found = True

    
    
    if found == False:
        print(guess_num)
        guess_num += 1
    return



def player_input(marker):
    marker = ' '
    while marker not in ('X','O'):
        marker = input('Player 1.  Please choose "X" or "O": ')
        marker = marker.upper()
    return marker   
    
def place_marker(man, marker, position):
    man[position] = marker

#Check if anyone won the game
def win_check(man, mark):
    
    if (man[1] == mark and man[2]== mark and man[3]==mark): 
        return True
    elif (man[4] == mark and man[5]== mark and man[6]==mark): 
        return True
    elif (man[7] == mark and man[8]== mark and man[9]==mark): 
        return True
    elif (man[1] == mark and man[4]== mark and man[7]==mark): 
        return True
    elif (man[2] == mark and man[5]== mark and man[8]==mark):
        return True
    elif (man[3] == mark and man[6]== mark and man[9]==mark):
        return True
    elif (man[1] == mark and man[5]== mark and man[9]==mark):
        return True
    elif (man[3] == mark and man[5]== mark and man[7]==mark):
        return True
    else:
        return False



# Return True if a space on the board is freely available.
def space_check(man, position):
    return man[position] == ' '


# function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_man_check(man):
    
    return man[1] != ' ' and man[2] != ' ' and man[3] != ' ' and man[4] != ' ' and man[5] != ' ' and man[6] != ' ' and man[7] != ' ' and man[8] != ' ' and man[9] != ' '
 



# function that asks for a player's next position (as a number 1-9) 
# and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(man):
         #Initial
    space_ok = False    
    choice = 'WRONG'
    acceptable_range = range(1,9+1)
    within_range = False   

        
    while choice.isdigit() == False or within_range == False or space_ok == False:
        choice = input('What position do you want? (1 - 9): ')
        
        # DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry that is not a digit")
        
        # RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False 
                print("Please enter 1 to 9")


        # SPACE AVAILABLE CHECK
        if choice.isdigit() == True:            
            if within_range == True:
                space_ok = space_check(man,int(choice))
                #print(f'space_ok: {space_ok}')
          
                    
    return int(choice)  

# Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    play_again = input('Would you like to play again? (Y/N): ')
    play_again = play_again.upper()
    if play_again == 'Y':
        return True
    else:
        return False



#--------------------------------------------------------------------
#--------------------------------------------------------------------



print('Welcome to Hang Man!')

while True:

    
    if guess_num == 1:
        # Choose a word...
        mylist = ["APPLES", "ORANGE", "BANANA" ]
        returnedword = (random.choice(mylist))
        word = str(returnedword)
        

        wordList = [letter for letter in word]
        one, two, three, four, five, six = wordList

    display_man(guess_num)
    make_a_guess()
    #guess_num += 1
     
                   
            
    if guess_num >= 7:
        print("You lose sucker!")
        print(f'The word was: {returnedword}')
        break
          
            
    #x = str("Hello" "World")
    #print(x[1])
    # prints e

    #==========================================================
#fruit_list = ['apple', 'orange', 'peach', 'pear', 'plum']

#x = fruit_list[0]

       
#wordList = [ch for ch in x]
#one, two, three, four, five = wordList
#print(str(one))
#print(str(two))