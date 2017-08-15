import random
import time
def intro():
    print """You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight. """
def choosecave():
    choose = input("Which cave would you proceed: (1) or (2)")
    if (choose != 1 and choose !=2):
        print "Number between 1 and 2"
        choosecave()
    return choose
def checkcave():
    time.sleep(1)
    print "You approach the cave..."
    time.sleep(1)
    print "It is dark and spooky..."
    time.sleep(1)
    print "A large dragon jumps out in front of you! He opens his jaws and..."
    time.sleep(1)
    friendlycave = random.randint(1,2)
    if xho == friendlycave:
        print "share his treasure with you."
    else:
        print "Gobbles you down in one bite!"
play = 'y'
while play == 'y':
    intro()
    xho = choosecave()
    checkcave()
    play = raw_input("Do you want to play again(y)").lower()[0]



