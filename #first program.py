# first program


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

def display():
    print('\n'*50)
    print(row1)
    print(row2)
    print(row3)

def make_ur_mark():
    global row1
    global row2
    global row3

    global player
    player = ' '
    while player not in ['X','O']:
        player = input("Are you X or O?").upper()

    def player_input():
        rowid_to_change = '0'
        while rowid_to_change not in ['1','2','3']:
            rowid_to_change = input("top to bottom what row would you like to mark?")

        position_to_change = 5
        while position_to_change not in [0,1,2]:
            position_to_change = int(input("left to right what square do you want to mark?"))-1
        return rowid_to_change, position_to_change

    rowid_to_change,position_to_change = player_input()
    if rowid_to_change == '1' and row1[position_to_change] == ' ':
        row1[position_to_change] = player

    elif rowid_to_change == '1' and row1[position_to_change] != ' ':
        print("that space is taken")
        
    elif rowid_to_change == '2' and row2[position_to_change] == ' ':
        row2[position_to_change] = player

    elif rowid_to_change == '2' and row2[position_to_change] != ' ':
        print("that space is taken")

    elif rowid_to_change == '3' and row3[position_to_change] == ' ':
        row3[position_to_change] = player

    elif rowid_to_change == '3' and row3[position_to_change] != ' ':
        print("that space is taken")


    return row1,row2,row3

def ask_keep_playing():
    ask_again = True
    while ask_again == True:
        yes_no = input('yes or no, you would like to keep playing?')
        if yes_no.lower() == 'yes':
            ask_again = False
            return True
        elif yes_no.lower() == 'no':
            ask_again = False
            return False
        else:
            print("I didnt understand that")

def check_for_win():

    if (row1[0] == row1[1] == row1[2] == 'X'):
        print("X is the winner")
        return False
    elif (row2[1] == row2[2] == row2[0] == 'X'):
        print("X is the winner")
        return False
    elif (row3[1] == row3[2] == row3[0] == 'X'):
        print("X is the winner")
        return False
    elif (row1[0] == row2[0] == row3[0] == 'X'):
        print("X is the winner")
        return False
    elif (row1[1] == row2[1] == row3[1] == 'X'):
        print("X is the winner")
        return False
    elif (row1[2] == row2[2] == row3[2] == 'X'):
        print("X is the winner")
        return False
    elif (row1[0] == row2[1] == row3[2]  == 'X'):
        print("X is the winner")
        return False
    elif (row1[2] == row2[1] == row3[0]  == 'X'):
        print("X is the winner")
        return False
    elif (row1[0] == row1[1] == row1[2] == 'O'):
        print("O is the winner")
        return False
    elif (row2[1] == row2[2] == row2[0] == 'O'):
        print("O is the winner")
        return False
    elif (row3[1] == row3[2] == row3[0] == 'O'):
        print("O is the winner")
        return False
    elif (row1[0] == row2[0] == row3[0] == 'O'):
        print("O is the winner")
        return False
    elif (row1[1] == row2[1] == row3[1] == 'O'):
        print("O is the winner")
        return False
    elif (row1[2] == row2[2] == row3[2] == 'O'):
        print("O is the winner")
        return False
    elif (row1[0] == row2[1] == row3[2]  == 'O'):
        print("O is the winner")
        return False
    elif (row1[2] == row2[1] == row3[0]  == 'O'):
        print("O is the winner")
        return False
    elif ' ' not in row1 and ' ' not in row2 and ' ' not in row3:
        print("Stalemate!")
        return False
    else:
         return True

cont_play = True
want_to_play = True
while cont_play == True:
    want_to_play = ask_keep_playing()
    if want_to_play == False:
        break
    make_ur_mark()
    display()
    cont_play = check_for_win()
    