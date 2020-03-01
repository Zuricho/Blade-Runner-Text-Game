import random
import person
import bladerunner


def dayBreak(time,MyCity,randomSeed):
    time = (time//100)*100+25
    print('*************************')
    print('What do you want to do today?')
    breakfast(time,MyCity,randomSeed)


def breakfast(time,MyCity,randomSeed):
    time = time+5
    for i in range(15):
        MyCity.DistrictList[i].infectRefresh(randomSeed,time)
    work(time,MyCity,randomSeed)
    pass


def work(time,MyCity,randomSeed):
    time = time+20
    for i in range(15,30):
        MyCity.DistrictList[i].infectRefresh(randomSeed,time,MyCity)

    if time%100 == 50:
        lunch(time,MyCity,randomSeed)
    elif time%100 == 75:
        dinner(time,MyCity,randomSeed)
    else:
        pass
    pass


def lunch(time,MyCity,randomSeed):
    time = time+5
    work(time,MyCity,randomSeed)
    pass


def dinner(time,MyCity,randomSeed):
    time = time+10
    for i in range(15):
        MyCity.DistrictList[i].infectRefresh(randomSeed,time)
    investigate(time,MyCity,randomSeed)
    pass


def investigate(time,MyCity,randomSeed):
    print('1-Visit A Place')
    print('2-Work')
    print('3-Pass&Rest')
    print('4-End Game and Report Bladerunner')
    choice = makeChoice(4)
    if choice == 1:
        placeNum = int(input('Where do you want to visit, use place number(0 to 29):'))
        visit(placeNum,MyCity)
        dayEnd(time,MyCity,randomSeed)
    elif choice == 2:
        print('You continue working! Money earned!')
        dayEnd(time,MyCity,randomSeed)
    elif choice == 3:
        dayEnd(time,MyCity,randomSeed)
    elif choice ==4:
        pass
    else:
        print('Wrong choice!')
        investigate(time,MyCity,randomSeed)
    pass


def dayEnd(time,MyCity,randomSeed):
    print('*************************')
    print("It's the end of your day!")
    print("It's your %d day in this city."%(time//100))
    time += 100
    dayBreak(time,MyCity,randomSeed)
    pass


def visit(placeNum,MyCity):
    Dist = MyCity.DistrictList[placeNum]
    print('What do you want to learn here?\n1-number of infected people here\n2-random ask one people here\nenter-skip')
    choice1 = makeChoice(3)
    if choice1 == 1:
        if placeNum in range(15,25):
            Dist.printWorkerList(MyCity)
            print("There are %d infected people here."%len(Dist.infectCount(MyCity)))
        elif placeNum in range(25,30):
            Dist.printStudentList(MyCity)
            print("There are %d infected people here."%len(Dist.infectCount(MyCity)))
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
    elif choice1 == 3:
        askedNum = int(input('ID of who you want to ask:'))
        if placeNum in range(25,30):
            if Dist.findStudent(askedNum) == True:
                print('Yes he/she is here!')
        elif placeNum in range(20,25):
            if Dist.findWorker(askedNum) == True:
                print('Yes he/she is here!')
    else:
        pass

    
def makeChoice(num):
    choice = input('Your choice number here:')
    if int(choice) in range(1,num+1):
        return int(choice)
    else:
        return 0


    
