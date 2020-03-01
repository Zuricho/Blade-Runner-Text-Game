import random


f_head = ['m','d','c','p','l','s','j','f','b','g','h','t','k','y','r','w','qu','n','wh','ch']
a_mid = ['a','e','i','o','u','ee','ai','ou','oi','au','oo','ui','ee','ea','oa','igh']
a_tail = ['er','ir','ur','ay','ow','oy','aw','ing','ung','eng','ang','ong','ew','ar','or','ed','ey']
f_tail = ['th','sh','ch','e','ck','t','d','b','k']


'''
type defination:
0: bubu
1: bu
2: bubud
3: bubay
4: bay
5: bud
'''
def chooseType():
    typeNum = random.randint(1,18)
    typeDic = {1:0,2:1,3:1,4:2,5:2,6:2,7:3,8:3,9:3,10:4,11:4,12:4,13:4,14:5,15:5,16:5,17:5,18:5}
    return typeDic[typeNum]


def type0Name():
    nameNum_0 = random.randint(1,20)
    nameNum_1 = random.randint(1,16)
    nameNum_2 = random.randint(1,20)
    nameNum_3 = random.randint(1,16)
    return f_head[nameNum_0-1]+a_mid[nameNum_1-1]+f_head[nameNum_2-1]+a_mid[nameNum_3-1]


def type1Name():
    nameNum_0 = random.randint(1,20)
    nameNum_1 = random.randint(1,16)
    return f_head[nameNum_0-1]+a_mid[nameNum_1-1]


def type2Name():
    nameNum_0 = random.randint(1,20)
    nameNum_1 = random.randint(1,16)
    nameNum_2 = random.randint(1,20)
    nameNum_3 = random.randint(1,16)
    nameNum_4 = random.randint(1,9)
    return f_head[nameNum_0-1]+a_mid[nameNum_1-1]+f_head[nameNum_2-1]+a_mid[nameNum_3-1]+f_tail[nameNum_4-1]


def type3Name():
    nameNum_0 = random.randint(1,20)
    nameNum_1 = random.randint(1,16)
    nameNum_2 = random.randint(1,20)
    nameNum_3 = random.randint(1,17)
    return f_head[nameNum_0-1]+a_mid[nameNum_1-1]+f_head[nameNum_2-1]+a_tail[nameNum_3-1]


def type4Name():
    nameNum_0 = random.randint(1,20)
    nameNum_1 = random.randint(1,17)
    return f_head[nameNum_0-1]+a_tail[nameNum_1-1]


def type5Name():
    nameNum_0 = random.randint(1,20)
    nameNum_1 = random.randint(1,16)
    nameNum_2 = random.randint(1,9)
    return f_head[nameNum_0-1]+a_mid[nameNum_1-1]+f_tail[nameNum_2-1]


def nameGenerate(randomSeed=None):
    # Usage: nameGenerate(randomSeed)
    random.seed(a=randomSeed)
    typeNum = chooseType()
    name = 'Default'
    if typeNum == 0:
        name = type0Name()
    elif typeNum == 1:
        name = type1Name()
    elif typeNum == 2:
        name = type2Name()
    elif typeNum == 3:
        name = type3Name()
    elif typeNum == 4:
        name = type4Name()
    elif typeNum == 5:
        name = type5Name()
    return name.capitalize()

