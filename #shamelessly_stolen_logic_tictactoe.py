#shamelessly stolen logic tictactoe

position_display_board = ['1','2','3','4','5','6','7','8','9']
#print(position_display_board[0])
the_board = [' ']*9
def display_board(board):
    
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[6]+'|'+board[7]+'|'+board[8])

player1 = ' '
player2 = ' '

def chose_ur_token():
    global player1
    global player2
    user_select = 'blank'
    while user_select not in ('X','O'):
        user_select = input('Player 1 are you X or O?').upper()
    if user_select == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'

place_chosen = 11
def chose_ur_place():
    player_input = ' '
    def check_if_unoccupied():
        global the_board
        if the_board[player_input] != ' ':
            return False
        else:
            return True

    while player_input not in (0,1,2,3,4,5,6,7,8):
        try:
            player_input = int(input('Where would you like to put your token? '))-1 
        #this subtraction lines up index position with display board positions
        except ValueError:
            print('Please use a valid board position')
            continue

        if check_if_unoccupied() == False:
            print("That space is occupied")
            player_input = 11
        else:
            return player_input
# I put validation to prevent overwriting spaces directly into the function

def check_for_win(player):
    global game_on
    if ((the_board[0] == the_board[1] == the_board[2] == player) 
    or (the_board[3] == the_board[4] == the_board[5] == player) 
    or (the_board[6] == the_board[7] == the_board[8] == player) 
    or (the_board[0] == the_board[4] == the_board[8] == player) 
    or (the_board[2] == the_board[4] == the_board[6] == player)
    or (the_board[0] == the_board[3] == the_board[6] == player)
    or (the_board[1] == the_board[4] == the_board[7] == player)
    or (the_board[2] == the_board[5] == the_board[8] == player)):
        print('The winner is '+player)
        game_on = False
    elif ' ' not in the_board:
        print('stalemate!')
        game_on = False

#the game
print('\n'*50)
print('Welcome, these are the names of the spaces to chose from')
display_board(position_display_board)
chose_ur_token()
game_on = True
playing = True
while playing:

    #first turn
    print("Player 1's turn")
    place_chosen = chose_ur_place()        
    the_board[place_chosen] = player1
    print('\n'*50)
    check_for_win(player1)
    display_board(the_board)
    if game_on == False:
        break
    
    #player 2's turn
    print("Player 2's turn")
    place_chosen = chose_ur_place()
    
    the_board[place_chosen] = player2
    print('\n'*50)
    check_for_win(player2)
    display_board(the_board)
    if game_on == False:
        break
    keep_playing = ' '
    while keep_playing not in ('y','yes','n','no'):
        keep_playing = input('Would you like to keep playing? Y/N ').lower()
    if keep_playing in ('n','no'):
        playing = False