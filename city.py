import random


class City:
    DistrictList = []
    def __init__(self,name,DistrictList):
        self.name = name
        self.DistrictList = DistrictList


# District type: 0 for living spaces(15), 1 for factory(10), 2 for school(5)
class District:
    def __init__(self,number,typenum):
        self.num = number
        self.type = typenum


def cityInit(cityName):
    MyCity = City(cityName,[])
    print('Welcome to city '+cityName+'!')
    
    for i in range(30):
        if i in range(15):
            MyCity.DistrictList.append(District(i,0))
        elif i in range(15,25):
            MyCity.DistrictList.append(District(i,1))
        else:
            MyCity.DistrictList.append(District(i,2))
    
    return MyCity

