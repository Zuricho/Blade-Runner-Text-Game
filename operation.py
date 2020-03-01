import random
import person
import bladerunner


def dayBreak(time,MyCity):
    time = (time//100)*100+25
    print('*************************')
    print('What do you want to do today?')
    breakfast(time,MyCity)


def breakfast(time,MyCity):
    time = time+5
    work(time,MyCity)
    pass


def work(time,MyCity):
    time = time+20
    for i in range(15,30):
        MyCity.DistrictList[i].infectRefresh(20200229,time)

    if time%100 == 50:
        lunch(time,MyCity)
    elif time%100 == 75:
        dinner(time,MyCity)
    else:
        pass
    pass


def lunch(time,MyCity):
    time = time+5
    work(time,MyCity)
    pass


def dinner(time,MyCity):
    time = time+10
    investigate(time,MyCity)
    pass


def investigate(time,MyCity):
    print('1-Visit A Place')
    print('2-Work')
    print('3-Pass&Rest')
    print('4-End Game and Report Bladerunner')
    choice = makeChoice(4)
    if choice == 1:
        placeNum = int(input('Where do you want to visit, use place number(0 to 29):'))
        visit(placeNum,MyCity)
        dayEnd(time,MyCity)
    elif choice == 2:
        print('You continue working! Money earned!')
        dayEnd(time,MyCity)
    elif choice == 3:
        dayEnd(time,MyCity)
    elif choice ==4:
        pass
    else:
        print('Wrong choice!')
        investigate(time,MyCity)
    pass


def dayEnd(time,MyCity):
    print('*************************')
    print("It's the end of your day!")
    print("It's your %d day in this city."%(time//100))
    time += 100
    dayBreak(time,MyCity)
    pass


def visit(placeNum,MyCity):
    Dist = MyCity.DistrictList[placeNum]
    print('What do you want to learn here?\n1-number of infected people here\n2-random ask one people here\nenter-skip')
    choice1 = makeChoice(2)
    if choice1 == 1:
        if placeNum in range(15,25):
            Dist.printWorkerList()
            print("There are %d infected people here."%len(Dist.infectCount()))
        elif placeNum in range(25,30):
            Dist.printStudentList()
            print("There are %d infected people here."%len(Dist.infectCount()))
        else:
            Dist.printHouseholdList()
            print("There are %d infected people here."%len(Dist.infectCount()))
        
    elif choice1 == 2:
        askedNum = input('ID of who you want to ask:')
        if askedNum == '':
            personList = person.personIDList()
            askedNum = personList[random.randint(0,29999)]
        else:
            askedNum = int(askedNum)
        AskedPerson = person.locate(askedNum,MyCity)
        print('You asked %s.'%AskedPerson.name)
        print('His job is %s.'%AskedPerson.jobName())
        print('He works at %d.'%AskedPerson.workplace)
        AskedPerson.getStatus()
        input('Press Enter to pass......')
    else:
        pass

    
def makeChoice(num):
    choice = input('Your choice number here:')
    if int(choice) in range(1,num+1):
        return int(choice)
    else:
        return 0


    
