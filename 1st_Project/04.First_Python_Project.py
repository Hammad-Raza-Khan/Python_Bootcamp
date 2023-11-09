# Step 1
# Write a function that can print out a board. Set up your board as a list, 
# where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.
def display_board(board):
    print('\n'*100)
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


         
#TEST Step 1: run your function on a test version of the board list, and make adjustments as necessary
test_board = ['#','X','O','X','O','X','O','X','O','X']


#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_input():
     marker=''
     while not(marker == 'X' or marker == 'O'):
         marker=input("Choose your Marker, player1 -> (X or O)").upper()
         
     
     if marker=='X':
         return('X', 'O')
     
     else:
         return('O', 'X')
     


#-------------------------------------------------

#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position]= marker
    
    
    
#Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


#Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.
import random

def choose_first():
    flip= random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'


#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    return board[position]==' '
    
            
#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


#Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again
def replay():
    choice=input('Do you want to play again ?  Y or N: \n')
    
    return choice== 'Y'








#Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!



while True:
    # Set the game up here
    print('\n'*100)
    print('Welcome to Tic Tac Toe!')
    
    #Setting everything up(BOARD, WHO IS GOING FIRST, CHOOSING MARKERS- X OR O)
    
    print("Welcome to Hammad's Tic-Tac-Toe; Let's start the game !! \n")
    test_board=[' ']*10
    
    player1_marker, player2_marker=player_input()

    turn=choose_first()
    print(turn + ' will go first ! ')
    
    play= input('Are You Ready To Play ? Y OR N')
    
    if play == 'Y':
        gameon= True
    else:
        gameon=False
    
    # GAME ON 
    
    while gameon:
        
        if turn=='Player 1':
            
            #display board
            display_board(test_board)
            
            #Choose a position/Input/ Select a position to start the game
            position= player_choice(test_board)
            
            #Place A Marker on it
            place_marker(test_board, player1_marker, position)
            
            #Check if won
            if win_check(test_board, player1_marker):
                display_board(test_board)
                print("Player 1 has WON !!")
                gameon=False
            #Check if tie
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("It is a Tie !")
                    break
                else:
                    turn= 'Player 2'

            #If nothing, next player's turn
        else:
            
            display_board(test_board)
            position= player_choice(test_board)
            place_marker(test_board, player2_marker, position)
            
            if win_check(test_board, player2_marker):
                display_board(test_board)
                print("Player 2 Has Won The Game !")
                gameon=False
                
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("It is a Tie !!")
                    break
                else: 
                    turn= 'Player 1'
                

    if not replay():
        break 
