import random
import nameGenerator


class Person:
    def __init__(self,number,name,job,status):
        self.ID = number
        self.name = name
        self.job = job
        # Job description should refer to readme
        self.status = status
        # status: 0-healthy, 1-first generation infected, 2-seconde generation infected
    def getStatus(self):
        if self.status == 0:
            print('you are healthy!')
        else:
            print('you are infected!')
    

def personInit(number,randomSeed):
    name = nameGenerator.nameGenerate(randomSeed*1000000+number)
    MyPerson = Person(number,name,0,0)
    return MyPerson


def locate(number,MyCity):
    disNum=number//10000
    buildNum=(number//1000)%10
    levelNum=(number//10)%100
    roomNum=number%10
    return MyCity.DistrictList[disNum].BuildingList[buildNum].LevelList[levelNum].RoomList[roomNum].PersonList[0]


