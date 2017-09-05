import random
import os
import time
print ("This game is brought to you by")
time.sleep(1)
print ("Niraj Budhathoki Company")
time.sleep(1)
print ("If you have any suggestion please email")
time.sleep(1)
print ("nirajcit@gmail.com")
time.sleep(3)
os.system('cls')
words = " moon word uber tiger elephant house mouse computer cartoon program character phone laptop ".lower().split()
def ranword():
    randword = words[random.randint(0,(len(words)-1))]
    return randword

def guess():
    guesslet = input("Guess the letter: ").lower()
    return guesslet

hangpic = ['''
    +-----+
          |
          |
          |
          |
  ===========        
''','''
    +-----+
    o     |
          |
          |
          |
  =========== 
''','''
    +-----+
    o     |
   /|     |
          |
          |
  =========== 
''','''
    +-----+
    o     |
   /|\    |
          |
          |
  ===========
''','''
    +-----+
    o     |
   /|\    |
          |
          |
  ===========
''','''
    +-----+
    o     |
   /|\    |
    |     |
          |
  ===========
''','''
    +-----+
    o     |
   /|\    |
    |     |
     \    |
  ===========

''','''
    +-----+
    o     |
   /|\    |
    |     |
   / \    |
  ===========
'''
]
play = 'y'
while play == 'y':
    os.system('cls')
    guessed = ''
    missfire = 0
    win = 0
    missed = ''
    rankword = ranword()
    blanks = '_' * len(rankword)
    while True:
        mk = 0
        print (hangpic[missfire])
        print ("Missed Letter: ", missed)
        print ("you have %s chance to go" % (7 - missfire))
        for i in blanks:
            print (i, end =' ')
        print()
        guesslet = guess()
        if len(guesslet) != 1:
            print ("Please enter just one letter")
            time.sleep(2)
        elif guesslet not in 'abcdefghijklmnopqrstuvwxyz':
            print ("please enter letter")
            time.sleep(2)
        elif guesslet in missed:
            print ("You have already missed that letter")
            time.sleep(2)
        elif guesslet in guessed:
            print ("you have already guessed that letter")
            time.sleep(2)
        elif guesslet in rankword:
            f = rankword.count(guesslet)
            win += f
            guessed += guesslet
            man = list(blanks)
            blanks = ''
            #i = rankword.find(guesslet) *it just find out first occurance only
            for jk in rankword:# replace blanks with correctly guessed letters
                if jk == guesslet:
                    man[mk] = guesslet
                mk += 1
            for i in man:
                blanks = blanks + i
        else:
            print ("you have missed the letter")
            missed += guesslet
            missfire += 1
        if win == len(rankword):
            print ("you won the game")
            print (rankword)
            break
        if missfire == 7:
            print ("you lose the game")
            print (rankword)
            break
    play = ''
    while not (play == 'y' or play == 'n'):
        play = input("Do you want to play it again(y) or (n)")







