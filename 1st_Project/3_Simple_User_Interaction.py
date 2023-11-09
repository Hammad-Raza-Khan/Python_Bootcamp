# A function for displaying current list:
game_list= ['0','1','2']
def display_game(game_list):
    print("Here is the current game list ")
    print(game_list)
#print(display_game(game_list))



# A function to check the input/range
def check_input():
    choice="Aevi"
    
    while choice not in ['0','1','2']:
        
        choice=input("Pick a number between ['0','1','2']: ")
        
        if choice not in ['0','1','2']:
            print("Wrong input ! ")
    return int(choice)
#print(check_input())



#Adding Replacement
def replacement(game_list, position):
    user_input= input("Enter a string to place at position: ")
    game_list[position]= user_input
    return game_list
#print(replacement(game_list, 0))



#A function that checks the input  to make it more user interactive:-
def game_on():
    choice="Aevi"
    
    while choice not in ['Y', 'N']:
        
        choice=input("Keep Playing ? [Y or N]: ")
        
        if choice not in ['Y','N']:
            print("Invalid Input ")
    if choice=='Y':
        return True
    else:
        return False
#print(check_input())

#-------------------------------------------------#

# PUTTING ALL OF THEM TOGETHER -
game_must_go_on= True
game_list= [0,1,2]

while game_must_go_on:
    
    display_game(game_list)
    
    position= check_input()
    
    game_list= replacement(game_list, position)
    
    display_game(game_list)
    
    game_must_go_on= game_on()