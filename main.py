# Game Name: Blade Runner Text Game
# Author: Zuricho Zhong
# Start Date: Feb 29, 2020
# Welcome to my game. Run this file to start game
# Hope you can enjoy your self here

import random
import nameGenerator
import city, building, person
import bladerunner
import storyteller
import operation


def main():
    # Random seed initialize
    randomSeed = input('Random seed, press ENTER to pass:')
    if randomSeed != '':
        randomSeed = int(randomSeed)
    else:
        randomSeed = 20200229
    random.seed(a=randomSeed)


    # Player name
    playerName = input('Your Character Name:')
    if playerName == '':
        playerName = nameGenerator.nameGenerate()
        print('Your name is %s!'%playerName)


    # City initiate
    cityName = 'unnamed city'
    cityName = input('Your City Name:')
    if cityName == '':
        cityName = nameGenerator.nameGenerate()
    MyCity = city.cityInit(cityName,randomSeed)


    # Myself initialize
    mSelfID = bladerunner.bladerunnerInit(randomSeed+1)
    mSelf = person.locate(mSelfID,MyCity)
    mSelf.name = playerName
    storyteller.bgTeller(mSelf.name,mSelf.ID)


    # Time and person list initialize
    personIDList = person.personIDList()
    time = 100


    # Day loop begin
    operation.dayBreak(time,MyCity)


    # Day loop end
    bladerunner.findBladerunner(MyCity.bRunnerID)


    # test block
    print('Bladerunner ID is: %d'%MyCity.bRunnerID)
    bRunner = person.locate(MyCity.bRunnerID,MyCity)
    print('Bladerunner Job is :',bRunner.jobName(),', work in ',bRunner.workplace)
    storyteller.endGame(playerName)



if __name__ == "__main__":
    main()
