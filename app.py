import time 

####   EXCUSE THE MESSY CODE, BUT IT DOES AT LEAST WORK !! ####

current_player = "X"
stop = False
board = [
    "-","-","-",
    "-","-","-",
    "-","-","-",
]

def declaration_of_winner():
    global current_player
    if (current_player == "draw"):          # because of the ordering I have to swap the X or O to get the correct winner!
        current_player == "X"
        new_game()
    else:
            if (current_player == "X"):
                current_player = "O"
                print("Player "+ current_player +" is the winner!")
            else:
                current_player = "X"
                print("Player "+ current_player +" is the winner!")
    play_again()
    


def play_again():
    global command
    command = input("Do you want to play again? (Y/N): ")
    if (command =="Y") or (command == "yes") or (command == "Yes")or (command == "y"):  # make it user friendly
        global board
        board = [                               # reset the board, and this is repeat code I know, but I'm rushed
        "-","-","-",
        "-","-","-",
        "-","-","-",
        ]
        new_game()
    else:
        print("see you next time dawg!")        
        quit()                                      # quitting python


def swap_player():
    global current_player                           # seems an excessive amount of global variables, I'm sure I could fix this...
    if (current_player == "X"):                 # after turn this changes the X to O and vice versa
        current_player = "O"
    else:
        current_player = "X"
    return current_player
    

def play_round():
    global command                              # seems an excessive amount of global variables, I'm sure I could fix this...
    if (command == "e"):                        # Quit if e is pressed
        quit() 
    command = int(command)
    if (board[command] == "-"):                 # check the place is blank
        del board[command]                      # remove the blank from the array
        board.insert(command, current_player)   # put in the X or O
        print_board()                           # print the updated board 
    else:
        print ("\n \n \n That square is taken, try again")      # if it wasn't blank already then it won't allow a change and 
        time.sleep(1.0)
        print(f"Player {current_player} please play again")     # force to play again
        #print_board()
    swap_player()
    check_for_winner()
    return
 
def check_for_winner():
    if (board[0]==board[1]==board[2] and board[0]!="-") or (board[3]==board[4]==board[5] and board[3]!="-") or (board[6]==board[7]==board[8] and board[6]!="-") or (board[0]==board[3]==board[6] and board[0]!="-") or(board[1]==board[4]==board[7] and board[1]!="-") or(board[2]==board[5]==board[8] and board[2]!="-") or(board[0]==board[4]==board[8] and board[0]!="-") or (board[6]==board[4]==board[2] and board[6]!="-"):
        declaration_of_winner()     ## Check if any 3 lines have the same (doesn't matter if x or o, and check the 3 the same are not the blank "-")
    elif (board[0]!="-" and board[1]!="-" and board[2]!="-" and board[3]!="-" and board[4]!="-" and board[5]!="-" and board[6]!="-" and board[7]!="-" and board[8]!="-"):
        print("It appears no-one has won... \nshall we try again...?") # see if all 9 squares are taken but not blank, then its a draw
        global current_player
        current_player="draw"                   # rename the player "draw" so the declaration_of_winner() fnc knows its a draw
        declaration_of_winner()
        new_game()                              # reset the board
    return False

def new_game():                 # reset the board... I think this code is in here 3x instead of 1... v sloppy
    global board
    current_player = "X"
    stop = False
    board = [
    "-","-","-",
    "-","-","-",
    "-","-","-",
    ]
    pass

def print_board():                              # same as your boiler plate, i added the 0,1,2 etc to make it easier to play
    print(f"""
    Current board ({current_player} turn):
        
    0,1,2 [{board[0]}] [{board[1]}] [{board[2]}]
    3,4,5 [{board[3]}] [{board[4]}] [{board[5]}]
    6,7,8 [{board[6]}] [{board[7]}] [{board[8]}]
    """)

def input_error():
        print ("You typed something wrong! \n You can type e to exit otherwise 0-8 only")      # just fixing mis-keys and devious users
        time.sleep(1.0)
        global command
        command = input("What do you want?: ")          # this is repeated but it solved some weird behaviour!

while stop == False:
    print_board()                                       
    command = input("What do you want?: ")
    while command not in ("0","1","2","3","4","5","6","7","8", "e"):
        input_error()            
    play_round() 
    if (command == "e"):
        stop = True
        quit()
    
    
