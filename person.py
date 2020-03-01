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
        self.workplace = None

    def getStatus(self):
        if self.status == 0:
            print('you are healthy!')
        else:
            print('you are infected!')

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
    

def personInit(number,randomSeed):
    name = nameGenerator.nameGenerate(randomSeed*1000000+number)
    MyPerson = Person(number,name,0,0)
    jobInit(MyPerson)
    return MyPerson


def locate(number,MyCity):
    disNum=number//10000
    buildNum=(number//1000)%10
    levelNum=(number//10)%100
    roomNum=number%10
    return MyCity.DistrictList[disNum].BuildingList[buildNum].LevelList[levelNum].RoomList[roomNum].PersonList[0]


def jobInit(Person):
    # Jobs: 1-HomeWorker; 2-Factory 3-Chef; 4-Student; 0-nojob
    IDnum = Person.ID
    random.seed(IDnum)
    jobnum = random.randint(1,30)
    if jobnum in range(1,11):
        Person.job = 1
        Person.workplace = Person.ID//10000
    elif jobnum in range(11,23):
        Person.job = 2
        Person.workplace = random.randint(15,24)
    elif jobnum in range(23,26):
        Person.job = 3
        Person.workplace = random.randint(0,29)
    else:
        Person.job = 4
        Person.workplace = random.randint(25,29)
    return 0
