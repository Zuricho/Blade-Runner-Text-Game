import random
import person


# Building Type: 0-High Building with 60 levels; 1-Meidum with 30; 2-Low with 20
class Building:
    LevelList = []
    def __init__(self,number,typenum,LevelList):
        self.num = number
        self.type = typenum
        self.LevelList = LevelList


class Level:
    RoomList = []
    def __init__(self,levelNum,RoomList):
        self.num = levelNum
        self.RoomList = RoomList


class Room:
    PersonList = []
    def __init__(self,number,PersonList):
        self.num = number
        self.PersonList = PersonList


def buildingInit0(number,randomSeed):
    MyBuilding = Building(number,0,[])
    for i in range(60):
        MyBuilding.LevelList.append(levelInit(number*100+i,randomSeed))
    return MyBuilding


def buildingInit1(number,randomSeed):
    MyBuilding = Building(number,0,[])
    for i in range(30):
        MyBuilding.LevelList.append(levelInit(number*100+i,randomSeed))
    return MyBuilding


def buildingInit2(number,randomSeed):
    MyBuilding = Building(number,0,[])
    for i in range(20):
        MyBuilding.LevelList.append(levelInit(number*100+i,randomSeed))
    return MyBuilding


def levelInit(number,randomSeed):
    MyLevel = Level(number,[])
    for i in range(10):
        MyLevel.RoomList.append(Room(number*10+i,[person.personInit(number*10+i,randomSeed)]))
    return MyLevel

