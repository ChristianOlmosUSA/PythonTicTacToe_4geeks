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
    if (current_player == "draw"):
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
    if (command =="Y") or (command == "yes") or (command == "Yes")or (command == "y"):
        global board
        board = [
        "-","-","-",
        "-","-","-",
        "-","-","-",
        ]
        new_game()
    else:
        print("see you next time dawg!")
        quit()


def swap_player():
    global current_player
    if (current_player == "X"):
        current_player = "O"
    else:
        current_player = "X"
    return current_player
    

def play_round():
    global command
    command = int(command)
    if (board[command] == "-"):
        del board[command]
        board.insert(command, current_player)
        print_board()
    else:
        print ("\n \n \n That square is taken, try again")
        time.sleep(1.0)
        print(f"Player {current_player} please play again")
        #print_board()
    swap_player()
    check_for_winner()
    return
 
def check_for_winner():
    
    if (board[0]==board[1]==board[2] and board[0]!="-") or (board[3]==board[4]==board[5] and board[3]!="-") or (board[6]==board[7]==board[8] and board[6]!="-") or (board[0]==board[3]==board[6] and board[0]!="-") or(board[1]==board[4]==board[7] and board[1]!="-") or(board[2]==board[5]==board[8] and board[2]!="-") or(board[0]==board[4]==board[8] and board[0]!="-") or (board[6]==board[4]==board[2] and board[6]!="-"):
        declaration_of_winner()
    elif (board[0]!="-" and board[1]!="-" and board[2]!="-" and board[3]!="-" and board[4]!="-" and board[5]!="-" and board[6]!="-" and board[7]!="-" and board[8]!="-"):
        print("It appears no-one has won... \nshall we try again...?")
        global current_player
        current_player="draw"
        declaration_of_winner()
        new_game()
        
    return False

def new_game():
    global board
    current_player = "X"
    stop = False
    board = [
    "-","-","-",
    "-","-","-",
    "-","-","-",
    ]
    pass

def print_board():
    print(f"""
    Current board ({current_player} turn):
        
    0,1,2 [{board[0]}] [{board[1]}] [{board[2]}]
    3,4,5 [{board[3]}] [{board[4]}] [{board[5]}]
    6,7,8 [{board[6]}] [{board[7]}] [{board[8]}]
    """)

def input_error():
        print ("\n \n \n incorrect item, please specify 0-8")
        time.sleep(1.0)
        global command
        command = input("What do you want?: ")

while stop == False:
    print_board()
    command = input("What do you want?: ")
    if (int(command) >= 9):
        input_error()        
    play_round() 
    if command == "stop":
        stop = True
    
    
