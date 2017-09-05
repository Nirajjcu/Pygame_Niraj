import os
def ask_Value(var):
    while True:
        try:
            val = int(input("please input integer value for %s: " %var))
            break
        except ValueError:
            print ("Oops seems like you entered something else")
    return val
def fibo(Start_Value,End_Value,How_long):
    'return fibonacci series'
    fibo = [Start_Value,End_Value]
    for i in range(How_long-2):
        fibo.append(fibo[-2]+fibo[-1])
    print (fibo)

play = 'y'
while play == 'y':
    print("Print values for fibonacci series")
    print("First enter starting value and then second value \n and the value that much you want fibonnaci numbers")
    x = ask_Value('starting value')
    y = ask_Value('second value')
    z = ask_Value('How long do you want')
    fibo(x,y,z)
    play = input("Do you want to play again(y) or (n): ")
    os.system('cls')



