import random
import nameGenerator


class Person:
    def __init__(self,number,name,job,status):
        self.ID = number
        self.name = name
        self.job = job
        # Jobs: 1-HomeWorker; 2-Factory 3-Chef; 4-Student; 0-nojob
        self.status = status
        # status: 0-healthy, 1-first generation infected, 2-seconde generation infected
        self.workplace = None

    def getStatus(self):
        if self.status == 0:
            print('%s is healthy!'%self.name)
        else:
            print('%s is infected!'%self.name)
            print('%s is the %d generation.'%(self.name,self.status))

    def location(self,time):
        # Location: 0-Home; 1-WorkPlace; 2-HomeRestaurant; 3-WorkRestaurant
        if time%100 in range(0,30)+range(85,100):
            return 0
        elif time%100 in range(30,50)+range(55,75):
            return 1
        elif time%100 in range(50,55):
            return 3
        else:
            return 2

    def districtNum(self):
        return self.ID//10000

    def buildingNum(self):
        return (self.ID//1000)%10

    def roomNum(self):
        return self.ID%1000

    def jobName(self):
        jobDict = {0:'no job',1:'home worker',2:'factory worker',3:'chef or waiter',4:'student'}
        return jobDict[self.job]



def locate(number,MyCity):
    disNum=number//10000
    buildNum=(number//1000)%10
    levelNum=(number//10)%100
    roomNum=number%10
    return MyCity.DistrictList[disNum].BuildingList[buildNum].LevelList[levelNum].RoomList[roomNum].PersonList[0]


def jobInit(randomSeed,num):
    # Jobs: 1-HomeWorker; 2-Factory 3-Chef; 4-Student; 0-nojob
    random.seed(randomSeed*100000+num)
    jobnum = random.randint(1,30)
    if jobnum in range(1,11):
        return [1,num//2000]
    elif jobnum in range(11,23):
        return [2,random.randint(15,24)]
    elif jobnum in range(23,26):
        return [3,random.randint(0,29)]
    else:
        return [4,random.randint(25,29)]


def personIDList():
    roomIDList = []
    for i in range(60):
        roomIDList.append(0*100+i)
    for i in range(60):
        roomIDList.append(1*100+i)
    for i in range(30):
        roomIDList.append(2*100+i)
    for i in range(30):
        roomIDList.append(3*100+i)
    for i in range(20):
        roomIDList.append(4*100+i)

    personIDList = []

    for j in range(15):
        districtIDList=[]
        for item in roomIDList:
            for i in range(10):
                districtIDList.append(item*10+i)
        for item in districtIDList:
            personIDList.append(j*10000+item)

    return personIDList


