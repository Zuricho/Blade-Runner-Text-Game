import time


def bgTeller(name,ID):
    print('Nice to meet you, %s.'%name)
    time.sleep(1)
    print('You are living in %d district, %d building, %d room.'%(ID//10000,(ID//1000)%10,ID%1000))
    time.sleep(1)
    print('Your task here is to find BLADERUNNER.')
    time.sleep(1)
    print('Who is BLADERUNNER?')
    time.sleep(1)
    print('BLADERUNNER is one person in this city, he/she spreads virus through the city, you need to find out where bladerunner lives, his/her name.')
    time.sleep(1)
    print("You can see other people's status, status number n means he/she is n generation of the virus, if status number is 1, it means you found bladerunner.")
    time.sleep(1)
    print("Begin your search!")
    time.sleep(1)


def endGame(playerName):
    print('Thank you for playing my game! %s'%playerName)
    print('Author: Züricho\nGithub: Zuricho')