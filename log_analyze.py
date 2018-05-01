f = open('.\\log\\log.txt',mode='r+')
lines = f.readlines()
for line in lines:
    time, = line.split(":")
