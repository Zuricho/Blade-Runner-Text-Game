import random
import building
import bladerunner
import person
import nameGenerator


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
                        Family.PersonList[0] = Family.PersonList[0]
                        if Family.PersonList[0].status == 0:
                            random.seed(a=randomSeed*10000+Family.PersonList[0].ID*100+time)
                            for source in infectList:
                                if Family.PersonList[0].status == 0 and random.randint(1,INFECT_RATE) == 1:
                                    Family.PersonList[0].status = source+1
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
                        if person.locate(studentID,MyCity).status == 0 and random.randint(1,INFECT_RATE) == 1:
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


def cityInit(randomSeed):
    MyCity = []
    for i in range(30000):
        personList = [i]
        personList.append(nameGenerator.nameGenerate(randomSeed*100000+i))   # Give him/her a name
        personList.append(num2ID(i))  # Living Place
        personList += person.jobInit(randomSeed,i)     # Job and Working place
        personList.append(0)  # status
        MyCity.append(personList)
    return MyCity


def num2ID(num):
    ID = (num//2000)*10000
    Buildin = num%2000
    if Buildin//600 in [0,1]:
        # tall builidngs with 60 floor
        ID += (Buildin//600)*1000+Buildin%600
    elif Buildin//300 in [4,5]:
        # mid buinding with 30 floor
        ID += ((Buildin//300)*1000)-2000+Buildin%300
    else:
        # low building with 20 floor
        ID += 4000+num%200
    return ID




