# Game Name: Blade Runner Text Game
# Author: Zuricho Zhong
# Start Date: Feb 29, 2020
# Welcome to my game. Run this file to start game
# Hope you can enjoy your self here

import random
import nameGenerator
import city
import building
import person



def main():
    # Random seed initialize
    randomSeed = 20200229
    randomSeed = int(input('Random seed, press ENTER to pass:'))
    random.seed(a=randomSeed)


    # Player name
    playerName = input('Your Character Name:')


    # City name
    cityName = 'unnamed city'
    cityName = input('Your City Name:')
    MyCity = city.cityInit(cityName,randomSeed)
    print(MyCity.DistrictList[0].type)
    print(MyCity.DistrictList[14].BuildingList[1].LevelList[15].RoomList[6].num)
    print(MyCity.DistrictList[14].BuildingList[1].LevelList[15].RoomList[6].PersonList[0].name)




if __name__ == "__main__":
    main()
