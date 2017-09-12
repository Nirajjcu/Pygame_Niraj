#print board
import os
import random
import time
def drawBoard(board): # Print Board
    print ("            |   |    ")
    print ("         "+board[6]+"  | "+board[7]+" | "+board[8]+"   ")
    print ("            |   |    ")
    print ("       --------------")
    print ("            |   |    ")
    print ("         "+board[3]+"  | "+board[4]+" | "+board[5]+"   ")
    print ("            |   |    ")
    print ("       --------------")
    print ("            |   |    ")
    print ("         "+board[0]+"  | "+board[1]+" | "+board[2]+"   ")
    print ("            |   |    ")

def CheckWin(PL):
    return ((Fillings[0] == PL and Fillings[1] == PL and Fillings[2] == PL) or
            (Fillings[3] == PL and Fillings[4] == PL and Fillings[5] == PL) or
            (Fillings[6] == PL and Fillings[7] == PL and Fillings[8] == PL) or
            (Fillings[0] == PL and Fillings[3] == PL and Fillings[6] == PL) or
            (Fillings[0] == PL and Fillings[4] == PL and Fillings[8] == PL) or
            (Fillings[1] == PL and Fillings[4] == PL and Fillings[7] == PL) or
            (Fillings[2] == PL and Fillings[5] == PL and Fillings[8] == PL) or
            (Fillings[6] == PL and Fillings[4] == PL and Fillings[2] == PL))



def choose(): #Choose if player wants X or O
    y = ''
    while not ( y == 'X' or y == 'O'):
        y = input("Do you want X or O: ").upper()
    return y

def CompTurn(): #Computer will randomly placed its move
    print("Now Computer's Turn")
    time.sleep(1)
    AIC = random.choice(k)
    k.remove(AIC)
    Fillings[AIC - 1] = AI
    drawBoard(Fillings)

def PlayerTurn():
    fi = ''
    while not (fi in k):
        fi = (int(input("Enter Your position(1-9): ")))
    k.remove(fi)
    Fillings[fi - 1] = g
    drawBoard(Fillings)

def TurnRandom():
    TR = random.randint(0,1)
    if TR == 1:
        print ("Player will go first")
    else:
        print ("Computer will go first")
    return TR

PLAY = 'y'
while PLAY == 'y':
    os.system('cls')
    g = choose()
    if g == 'X':
        AI = 'O'
    else:
        AI = 'X'
    print ("you have choose %s" %g)
    Fillings = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    k = [1,2,3,4,5,6,7,8,9]
    T_var = TurnRandom()
    gameISPlaying = True
    #print (len(Fillings))
    while gameISPlaying:
        if T_var == 1:
            PlayerTurn()
            CompTurn()
            var = CheckWin(g)
            if var == True:
                print ("you won the game: ")
                gameISPlaying = False
        else:
            CompTurn()
            PlayerTurn()
    print (Fillings)

    PLAY = input("Do you want to play again(y) or (n)").lower()






