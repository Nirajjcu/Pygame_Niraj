import random
hello = raw_input("Hello! What is your Name: ")
print "Hi ",hello, "I am thinking a number between 1 to 20"
#print "Take a guess"
guess = 0
count = 0
rank = random.randint(0,20)
while guess != rank:
    guess = input("Take a guess: ")
    if guess > rank:
        print "your guess is high"
    elif guess < rank:
        print "your guess is low"
    count += 1
print "Good job " + hello + " You guessed my number in " + str(count) + ' guess'

