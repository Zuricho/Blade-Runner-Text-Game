f = open("test.txt","w+")

a = [1,2,3,'test']
b = [1,2,3,'test']


f.write(str(a)[1:-1].replace("'","")+'\n')
f.write(str(b)[1:-1].replace("'","")+'\n')
