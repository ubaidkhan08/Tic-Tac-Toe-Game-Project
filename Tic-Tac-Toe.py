from IPython.display import clear_output

def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    

test_board = [' ']*10


def player_input():
    
    marker = ''
    while marker != 'X'  and marker != 'O': 
        marker = (input("Player-1, choose from X or O: ")).upper()
    
    if marker == 'X':
        return ('X', 'O')
    
    if marker == 'O':
        return ('O', 'X')
    
    
def place_marker(board, marker, position):
    board[position] = marker
    
    
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


import random

def choose_first():
    if random.randint(0,1) == 1:
        return "Player-1 GO!"
    
    else:
        return "Player-2 GO!"
    
    
def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    
    for i in range(1,10):
        
        if space_check(board, i) == True:
            return False 
        
        #if space_check(board, i) == False:
            #return True (DONT USE THIS LOGIC)
            
    return True #if the board doesn't return FALSE, it'll return TRUE!

full_board_check(test_board)


def player_choice(board):  
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    
    return position


def replay():
    
    PA = 'A'
    while PA != 'Y' or PA != 'N' :
        PA = (input("Do you wish to continue? (Y or N) ")).upper()

        if PA == 'Y':
            return True

        if PA == 'N':
            return False 
        
        
print('Welcome to Tic Tac Toe!\n')

while True:
    test_board = [' ']*10
    player1,player2 = player_input()
    print(f"Player-1 will be {player1}")
    print(f"Player-2 will be {player2}\n")
    
    turn = choose_first()
    print(choose_first())
    print('\n')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
        
    while game_on == True:
        if turn == 'Player-1 GO!':
            
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player1, position)
            
            if win_check(test_board,player1):
                display_board(test_board)
                print('Congratulations! Player-1 has won the game!')
                game_on = False

            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("It's a DRAW")
                    #game_on = False
                    break
                    
                else:
                    turn = 'Player-2 GO!'
                
        else:
            # Player2's turn.
            
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player2, position)

            if win_check(test_board, player2):
                display_board(test_board)
                print('Player-2 has won!')
                game_on = False
                
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player-1 GO!'
        
    if not replay():
        print("\nThank you for playing!")
        break