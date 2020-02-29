import random
import nameGenerator


class Person:
    def __init__(self,number,name,job,status):
        self.num = number
        self.name = name
        self.job = job
        # Job description should refer to readme
        self.status = status
        # status: 0-healthy, 1-first generation infected, 2-seconde generation infected
    

def personInit(number,randomSeed):
    name = nameGenerator.nameGenerate(randomSeed*1000000+number)
    MyPerson = Person(number,name,0,0)
    return MyPerson


