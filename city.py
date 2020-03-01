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
        return householdList

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
                        infectList.append(Household.status)
                    else:
                        pass
        return infectList

    def infectRefresh(self,randomSeed,time):
        INFECT_RATE = 30000    # The rate is 1/this number
        infectList = self.infectCount()
        if len(infectList) != 0:
            for Build in self.BuildingList:
                for Floor in Build.LevelList:
                    for Family in Floor.RoomList:
                        Household = Family.PersonList[0]
                        if Household.status == 0:
                            random.seed(a=randomSeed*10000+Household.ID*100+time)
                            for source in infectList:
                                if Household.status == 0 and random.randint(1,INFECT_RATE) == 1:
                                    Household.status = source+1
                                else:
                                    pass
                        else:
                            pass
        else:
            pass
        return 0 


class Factory:
    def __init__(self,number):
        self.num = number
        self.WorkerList = []
    
    def addWorker(self,workerID):
        self.WorkerList.append(workerID)

    def printWorkerList(self,MyCity,num=1000):
        i=0
        for workerID in self.WorkerList:
            worker = person.locate(workerID,MyCity)
            print(worker.name,end=',')
            i+=1
            if i >= num:
                print('\n')
                break

    def infectCount(self,MyCity):
        infectList = []
        for workerID in self.WorkerList:
            worker = person.locate(workerID,MyCity)
            if worker.status != 0:
                infectList.append(worker.status)
        return infectList

    def infectRefresh(self,randomSeed,time,MyCity):
        INFECT_RATE = 10000    # The rate is 1/this number
        infectList = self.infectCount(MyCity)
        if len(infectList) != 0:
            for workerID in self.WorkerList:
                worker = person.locate(workerID,MyCity)
                if worker.status == 0:
                    random.seed(a=randomSeed*10000+worker.ID*100+time)
                    for source in infectList:
                        if worker.status == 0 and random.randint(1,INFECT_RATE) == 1:
                            person.locate(workerID,MyCity).status = source+1
                        else:
                            pass
                else:
                    pass
        else:
            pass
        return 0

    def findWorker(self,ID):
        return ID in self.WorkerList

class School:
    def __init__(self,number):
        self.num = number
        self.StudentList = []
    
    def addStudent(self,studentID):
        self.StudentList.append(studentID)
    
    def printStudentList(self,MyCity,num=100):
        i=0
        for studentID in self.StudentList:
            student = person.locate(studentID,MyCity)
            print(student.name,end=',')
            i+=1
            if i >= num: 
                print('\n')
                break

    def infectCount(self,MyCity):
        infectList = []
        for studentID in self.StudentList:
            student = person.locate(studentID,MyCity)
            if student.status != 0:
                infectList.append(student.status)
        return infectList

    def infectRefresh(self,randomSeed,time,MyCity):
        INFECT_RATE = 5000
        infectList = self.infectCount(MyCity)
        if len(infectList) != 0:
            for studentID in self.StudentList:
                student = person.locate(studentID,MyCity)
                if student.status == 0:
                    random.seed(a=randomSeed*10000+student.ID*100+time)
                    for source in infectList:
                        if student.status == 0 and random.randint(1,INFECT_RATE) == 1:
                            person.locate(studentID,MyCity).status = source+1
                        else:
                            pass
                else:
                    pass
        else:
            pass
        return 0
    
    def findStudent(self,ID):
        return ID in self.StudentList


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
    bladerunner.bladerunnerLocate(bRunnerID,MyCity)
    MyCity.bRunnerInit(bRunnerID)

    # Align their work
    personIDList = person.personIDList()
    for ID in personIDList:
        citizen = person.locate(ID,MyCity)
        if citizen.job == 2:
            MyCity.DistrictList[citizen.workplace].addWorker(ID)
        elif citizen.job == 4:
            MyCity.DistrictList[citizen.workplace].addStudent(ID)
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



