import random
import building
import bladerunner
import person


class City:
    DistrictList = []
    def __init__(self,name,DistrictList):
        self.name = name
        self.DistrictList = DistrictList
        self.bRunnerID = None
    
    def bRunnerInit(self,bRunnerID):
        self.bRunnerID = bRunnerID


# District type: 0 for living spaces(15), 1 for factory(10), 2 for school(5)
class District:
    BuildingList = []
    def __init__(self,number,BuildingList):
        self.num = number
        self.BuildingList = BuildingList

    def getHouseholdList(self):
        householdList = []
        for Build in self.BuildingList:
            for Floor in Build.LevelList:
                for Family in Floor.RoomList:
                    householdList.append(Family.PersonList[0])

    def printHouseholdList(self,num=1000):
        i=0
        for Household in self.getHouseholdList():
            print(Household.name,end=',')
            i+=1
            if i >= num:
                print('\n')
                break
        print('\n')


    def infectCount(self):
        infectList = []
        for Build in self.BuildingList:
            for Floor in Build.LevelList:
                for Family in Floor.RoomList:
                    Household = Family.PersonList[0]
                    if Household.status != 0:
                        infectList.append(worker.status)
                    else:
                        pass
        return infectList


class Factory:
    def __init__(self,number):
        self.num = number
        self.WorkerList = []
    
    def addWorker(self,worker):
        self.WorkerList.append(worker)

    def printWorkerList(self,num=1000):
        i=0
        for worker in self.WorkerList:
            print(worker.name,end=',')
            i+=1
            if i >= num:
                print('\n')
                break

    def infectCount(self):
        infectList = []
        for worker in self.WorkerList:
            if worker.status != 0:
                infectList.append(worker.status)
        return infectList

    def infectRefresh(self,randomSeed,time):
        INFECT_RATE = 500    # The rate is 1/this number
        infectList = self.infectCount()
        if len(infectList) != 0:
            for worker in self.WorkerList:
                if worker.status == 0:
                    random.seed(a=randomSeed*10000+worker.ID*100+time)
                    for source in infectList:
                        if worker.status == 0 and random.randint(1,INFECT_RATE) == 1:
                            worker.status = source+1
                        else:
                            pass
                else:
                    pass
        else:
            pass
        return(time)

class School:
    def __init__(self,number):
        self.num = number
        self.StudentList = []
    
    def addStudent(self,student):
        self.StudentList.append(student)
    
    def printStudentList(self,num=100):
        i=0
        for student in self.StudentList:
            print(student.name,end=',')
            i+=1
            if i >= num: 
                print('\n')
                break

    def infectCount(self):
        infectList = []
        for student in self.StudentList:
            if student.status != 0:
                infectList.append(student.status)
        return infectList

    def infectRefresh(self,randomSeed,time):
        INFECT_RATE = 200
        infectList = self.infectCount()
        if len(infectList) != 0:
            for student in self.StudentList:
                if student.status == 0:
                    random.seed(a=randomSeed*10000+student.ID*100+time)
                    for source in infectList:
                        if student.status == 0 and random.randint(1,INFECT_RATE) == 1:
                            student.status = source+1
                        else:
                            pass
                else:
                    pass
        else:
            pass
        return(time)


def cityInit(cityName,randomSeed):
    MyCity = City(cityName,[])
    print('Welcome to city '+cityName+'!')
    print('Loading......')
    
    # Living place and all people
    for i in range(15):
        MyDistrict = districtInit0(i,randomSeed)
        MyCity.DistrictList.append(MyDistrict)

    # Factory
    for i in range(15,25):
        MyDistrict = districtInit1(i,randomSeed)
        MyCity.DistrictList.append(MyDistrict)

    # School
    for i in range(25,30):
        MyDistrict = districtInit2(i,randomSeed)
        MyCity.DistrictList.append(MyDistrict)

    # Bladerunner initialize
    bRunnerID = bladerunner.bladerunnerInit(randomSeed)
    bRunner = bladerunner.bladerunnerLocate(bRunnerID,MyCity)
    bRunner.status = 1
    MyCity.bRunnerInit(bRunnerID)

    # Align their work
    personIDList = person.personIDList()
    for ID in personIDList:
        citizen = person.locate(ID,MyCity)
        if citizen.job == 2:
            MyCity.DistrictList[citizen.workplace].addWorker(citizen)
        elif citizen.job == 4:
            MyCity.DistrictList[citizen.workplace].addStudent(citizen)
        else:
            pass

    return MyCity


def districtInit0(number,randomSeed):
    MyDistrict = District(number,[])
    for i in range(6):
        if i in [0,1,2]:
            MyDistrict.BuildingList.append(building.buildingInit0(MyDistrict.num*10+i,randomSeed))
        elif i in [3,4]:
            MyDistrict.BuildingList.append(building.buildingInit1(MyDistrict.num*10+i,randomSeed))
        else:
            MyDistrict.BuildingList.append(building.buildingInit2(MyDistrict.num*10+i,randomSeed))
    return MyDistrict


def districtInit1(number,randomSeed):
    MyDistrict = Factory(number)
    return MyDistrict


def districtInit2(number,randomSeed):
    MyDistrict = School(number)
    return MyDistrict



