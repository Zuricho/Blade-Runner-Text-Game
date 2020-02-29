import random
import building


class City:
    DistrictList = []
    def __init__(self,name,DistrictList):
        self.name = name
        self.DistrictList = DistrictList


# District type: 0 for living spaces(15), 1 for factory(10), 2 for school(5)
class District:
    BuildingList = []
    def __init__(self,number,typenum,BuildingList):
        self.num = number
        self.type = typenum
        self.BuildingList = BuildingList


def cityInit(cityName):
    MyCity = City(cityName,[])
    print('Welcome to city '+cityName+'!')
    
    for i in range(30):
        if i in range(15):
            MyDistrict = districtInit0(i)
            MyCity.DistrictList.append(MyDistrict)
        elif i in range(15,25):
            MyCity.DistrictList.append(District(i,1,[]))
        else:
            MyCity.DistrictList.append(District(i,2,[]))
    
    return MyCity


def districtInit0(number):
    MyDistrict = District(number,0,[])
    for i in range(6):
        if i in [0,1,2]:
            MyDistrict.BuildingList.append(building.buildingInit0(MyDistrict.num*10+i))
        elif i in [3,4]:
            MyDistrict.BuildingList.append(building.buildingInit1(MyDistrict.num*10+i))
        else:
            MyDistrict.BuildingList.append(building.buildingInit2(MyDistrict.num*10+i))
    return MyDistrict


# def districtInit1(number):



# def districtInit2(number):



