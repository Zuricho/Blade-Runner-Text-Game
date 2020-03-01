import random
import person


def dayBreak(time,MyCity):
    print('*************************')
    print('What do you want to do today?')
    print('1-Visit A Place')
    print('2-Work')
    print('3-Pass&Rest')
    choice = makeChoice(3)
    if choice == 1:
        placeNum = int(input('Where do you want to visit, use place number:'))
        visit(placeNum,MyCity)
        dayEnd(time,MyCity)
    elif choice == 2:
        print('You went working! Money earned!')
        dayEnd(time,MyCity)
    elif choice == 3:
        dayEnd(time,MyCity)
    else:
        print('Wrong choice!')
        dayBreak(time)


def dayEnd(time,MyCity):
    print('*************************')
    print("It's the end of your day!")
    print("It's your %d day in this city."%(time//100))
    time += 100
    dayBreak(time,MyCity)
    return time


def visit(placeNum,MyCity):
    print('What do you want to learn here?\n1-number of infected people here\n2-random ask one people here\nenter-skip')
    choice1 = makeChoice(2)
    if choice1 == 1:
        print('%d people infected'%0)
    elif choice1 == 2:
        askedNum = int(input('ID of who you want to ask:'))
        AskedPerson = person.locate(askedNum,MyCity)
        print('You asked %s.'%AskedPerson.name)
        print('His job is %s.'%AskedPerson.jobName())
        print('He works at %d.'%AskedPerson.workplace)
    else:
        pass

    
def makeChoice(num):
    choice = input('Your choice number here:')
    if int(choice) in range(1,num+1):
        return int(choice)
    else:
        return 0


    
