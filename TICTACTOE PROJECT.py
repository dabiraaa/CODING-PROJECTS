import random
print('Ready to play tictactoe')
img=''' The positions are labelled for you to make your move
                        |        |
                       0|     1  |   2
                 ______ |________|________
                        |        |
                     3  |   4    |    5
                _______ |________|________
                        |        |
                     6  |    7   |  8
                        |        |
'''
board = ["_", "_", "_",
        "_", "_", "_",
        "_","_", "_"]
#let human player be X and computer be O
user_player=input("You will play as X, enter X:")
computer='O'
#print tictactoe board
def printboard(board):
    print('|'+board[0]+'|'+board[1]+'|'+board[2]+'|'+'\n'
        +'|'+board[3]+'|'+ board[4]+'|'+ board[5]+'|'+'\n'
        +'|'+ board[6]+'|'+board[7]+'|' +board[8]+'|')
#let computer make a random move
def computer_move(board):
    position=random.randint(0,8)
    if board[position]=='_':
        board[position]=computer
    else:
        computer_move(board)
#tictactoe rules of playing
def player_move(board):
    print(img)
    position=int(input("Pick a position from 0 to 8:"))
    if position>=0 and position<=8 and board[position]=='_':
        board[position]=user_player
    elif board[position]!='_':
        print("That position has been played in")
    else:
        print("That's not a valid location")
#to check for winner
def winner():
#check for winner in columns
    if board[0]==board[1]==board[2]!='_':
        print(board[0]+" won!")
        return False
    elif board[3]==board[4]==board[5]!='_':
        print(board[3]+" won!")
        return False
    elif board[6]==board[7]==board[8]!='_':
        print(board[6] + " won!")
        return False
#check for winner in rows
    elif board[0]==board[3]==board[6]!='_':
        print(board[0] + " won!")
        return False
    elif board[1]==board[4]==board[7]!='_':
        print(board[1] + " won!")
        return False
    elif board[2]==board[5]==board[8]!='_':
        print(board[2] + " won!")
        return False
#check for winner diagonally
    elif board[0]==board[4]==board[8]!='_':
        print(board[0] + " won!")
        return False
    elif board[2]==board[4]==board[6]!='_':
        print(board[2] + " won!")
        return False
    else:
        return True
        print("No winner")

#TO START GAME
playing=True
while playing==True:
    printboard(board)
    player_move(board)
    computer_move(board)
    winner()
    if winner() == False:
        break


