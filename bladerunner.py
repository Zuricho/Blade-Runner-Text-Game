import random
import city
import building
import person


def bladerunnerInit(randomSeed):
    random.seed(a=randomSeed)

    disNum = random.randint(0,14)
    buildNumRan = random.randint(0,9)
    if buildNumRan in [0,1,2,3,4,5]:
        buildNum = random.randint(0,1)
        levelNum = random.randint(0,60)
    elif buildNumRan in [6,7,8]:
        buildNum = random.randint(2,3)
        levelNum = random.randint(0,30)
    else:
        buildNum = 4
        levelNum = random.randint(0,20)
    roomNum = random.randint(0,9)

    return disNum*10000+buildNum*1000+levelNum*10+roomNum


def bladerunnerLocate(number,MyCity):
    disNum=number//10000
    buildNum=(number//1000)%10
    levelNum=(number//10)%100
    roomNum=number%10
    MyCity.DistrictList[disNum].BuildingList[buildNum].LevelList[levelNum].RoomList[roomNum].PersonList[0].status=1
    return MyCity.DistrictList[disNum].BuildingList[buildNum].LevelList[levelNum].RoomList[roomNum].PersonList[0]


def findBladerunner(bladerunnerID):
    choice = input("Report bladerunner's ID:")
    findID = int(input('Input bladerunner ID here:'))
    if findID == bladerunnerID:
        print('YOU ARE RIGHT!\nCONGRADULATIONS!')
    else:
        choice2 = input('Sorry you are wrong. Input Q to quit game.')
        if choice2 == 'Q':
            pass
        else:
            findBladerunner(bladerunnerID)

