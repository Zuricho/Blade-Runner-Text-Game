import random


def dayBreak(time):
    print('What do you want to do today?')
    print('1-Visit A Place')
    print('2-Work')
    print('3-Pass&Rest')
    choice = makeChoice(3)
    if choice == 1:
        placeNum = int(input('Where do you want to visit, use place number:'))
        visit(placeNum)
        dayEnd(time)
    elif choice == 2:
        print('You went working! Money earned!')
        dayEnd(time)
    elif choice == 3:
        dayEnd(time)
    else:
        print('Wrong choice!')
        dayBreak(time)


def dayEnd(time):
    print('Your day ended!')
    print("It's your %d day in this city."%(time//100))
    time += 100
    dayBreak(time)
    return time


def visit(placeNum):
    print('What do you want to learn here?\n1-number of infected people here\n2-random ask one people here\nenter-skip')
    choice1 = makeChoice(2)
    if choice1 == 1:
        print('%d people infected'%0)
    elif choice1 == 2:
        print('You asked %s'%'random people')
    else:
        pass

    
def makeChoice(num):
    choice = input('Your choice number here:')
    if int(choice) in range(1,num+1):
        return int(choice)
    else:
        return 0


    
