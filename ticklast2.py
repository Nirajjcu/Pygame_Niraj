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

def CheckWin(PL): #Check the winining by player
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

def ifWin(symbol): #Check if computer can win
    global Fillings
    Temp = Fillings[:]
    for i in k:
        Fillings[i-1] = symbol

        if CheckWin(symbol):
            Fillings = Temp[:]
            return i

        Fillings = Temp[:]
    return False

def Corners(): #Take four corners if free
    tempList = []
    if Fillings[0] == ' ':
        tempList.append(1)
    if Fillings[2] == ' ':
        tempList.append(3)
    if Fillings[6] == ' ':
        tempList.append(7)
    if Fillings[8] == ' ':
        tempList.append(9)
    return tempList


def CompTurn(): #Computer will randomly place its move
    print("Now Computer's Turn")
    time.sleep(.5)
    forAI = ifWin(AI)
    forPL = ifWin(g)
    takeCorners = Corners()
    if forAI: #Check if computer can win with its move
        k.remove(forAI)
        Fillings[forAI -1] = AI
        drawBoard(Fillings)
    elif forPL: #Check if player can win its game and block it
        k.remove(forPL)
        Fillings[forPL -1] = AI
        drawBoard(Fillings)
    elif len(takeCorners) != 0: #Take corners if its free
        AIS = random.choice(takeCorners)
        k.remove(AIS)
        Fillings[AIS -1] = AI
        drawBoard(Fillings)
    elif Fillings[4] == ' ': #Take middle one if its free
        k.remove(5)
        Fillings[4] = AI
        drawBoard(Fillings)


    else: # Choose randomly from side spaces
        AIC = random.choice(k)
        k.remove(AIC)
        Fillings[AIC - 1] = AI
        drawBoard(Fillings)
        print ("this was exected to take side spaces")

def PlayerTurn():
    fi = ''
    while not (fi in k): #Until it becames blank
        fi = (int(input("Enter Your position(1-9): ")))
    k.remove(fi)
    Fillings[fi - 1] = g
    drawBoard(Fillings)

def TurnRandom():
    TR = random.randint(0,1)
    if TR == 1:
        TR = 'player'
        print ("Player will go first")
    else:
        print ("Computer will go first")
    return TR

def CheckTie(TT):
    if TT == 9:
        print ("The game is Tie")
        return True


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
    Turn = TurnRandom()
    gameISPlaying = True
    CK = 0
    while gameISPlaying:
        if Turn == 'player': #IF player gets 1st move this layer will be executed
            PlayerTurn()
            var = CheckWin(g)
            if var == True:
                print ("you won the game: ")
                break
            CK += 1 # To check if the board is full
            if CheckTie(CK):
                break
            Turn = 'computer'

        else: #if Computer gets its 1st move this layer will be executed
            CompTurn()
            var_AI = CheckWin(AI)
            if var_AI == True:
                print ("computer won the game: ")
                break
            CK += 1
            if CheckTie(CK):
                break
            Turn = 'player'
    print (Fillings)
    PLAY = input("Do you want to play again(y) or (n)").lower()
