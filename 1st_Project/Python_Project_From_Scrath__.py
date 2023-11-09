# Step 1
# Write a function that can print out a board. Set up your board as a list, 
# where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display(board):
    print('\n'*10)
    print(' ''  |  '' ''  |  '' ')
    print(board[1]+'  |  '+board[2]+'  |  '+board[3])
    print(' ''  |  '' ''  |  '' ')
    print('---------------')
    print(' ''  |  '' ''  |  '' ')
    print(board[4]+'  |  '+board[5]+'  |  '+board[6])
    print(' ''  |  '' ''  |  '' ')
    print('---------------')
    print(' ''  |  '' ''  |  '' ')
    print(board[7]+'  |  '+board[8]+'  |  '+board[9])
    print(' ''  |  '' ''  |  '' ')
    print("     ")
    
my_board=['#','X','O','X','O','X','O','X','O','X']

#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
#Think about using while loops to continually ask until you get a correct answer.

def marker_choice():
    marker=''
    while not(marker == 'X' or marker == 'O'):
        marker=input("Player 1, Kindly choose a marker-> (X or O) \n").upper()
        
    if marker == 'X' :
        return ('X', 'O')
    else:
        return ('O', 'X')


#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.

def assign(board, marker, position):
    board[position]= marker
    
#Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def checks_victory(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

#Step 5: Write a function that uses the random module to randomly decide which player goes first. 
#You may want to lookup random.randint() Return a string of which player went first.

import random

def who_goes_first():
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return 'Player 2'
    
#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def free_space_check(board, position):
    return board[position]== ' '

#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1,10):
        if free_space_check(board, i):
            return False
    return True
        
#Step 8: Write a function that asks for a player's next position (as a number 1-9) 
# and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def next_move(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not free_space_check(board, position):
        try:
            position = int(input("Choose a position from 1-9: \n"))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 9.")

    return position
    
        
    
#Step 9: Write a function that asks the player if they want to play again
# and returns a boolean True if they do want to play again

def play_again():
    ask=input("Do you want to continue or play again ? 'Y or N' : \n").upper()
    
    if ask=='Y':
        return True
    else:
        return False
    
#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

while True :
    
    
    print("\n"*60)
    print("Welcome to the TTT ! ")
    my_board= [' ']*10
    print("First, Assume anyone of you to be Player 1 !\n")
    
    print(" Let us assign a marker: \n")
    player1_marker, player2_marker=marker_choice()
    
    print("NOW, Let us see who will go first: ")
    turn=who_goes_first()
    print(turn + " will go first !")
    
    asking=input("\n Are you ready to continue ? \n Press Y for Yes or Press any Key to Discontinue :\n").upper()
    if asking=='Y':
        continues = True
    else:
        continues = False
    
    while continues:
        
        # Player 1 
        if turn == 'Player 1':
            display(my_board)
            
            position= next_move(my_board)
            
            assign(my_board, player1_marker, position)
    
            #win
            if checks_victory(my_board, player1_marker):
                display(my_board)
                print("Victory is to Player 1 ! ")
                continues=False
                
            else:
                if full_board_check(my_board):
                    display(my_board)
                    print("It is A Tie !")
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            display(my_board)
                
            position= next_move(my_board)
            assign(my_board, player2_marker, position)
                
            if checks_victory(my_board, player2_marker):
                display(my_board)
                print("Victory is to Player 2 ! ")
                continues=False
            else:
                if full_board_check(my_board):
                    display(my_board)
                    print("It is A Tie !")
                    break
                else:
                    turn = 'Player 1'
                    
    if not play_again():
                                 break
                    
        
    
    
    

