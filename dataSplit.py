mainSet = open('blkjckhands.csv', 'r')
testSet = open('blkjckTest.csv', 'w')
trainSet = open('blkjckTrain.csv', 'w')
devSet = open('blkjckDev.csv', 'w')

n = 0
for line in mainSet:

    if n == 0:
        testSet.write(line)
        trainSet.write(line)
        devSet.write(line)

    if  0 < n < 630002:
        trainSet.write(line)
    
    elif 630002 <= n < 720002:
        devSet.write(line)
    
    elif 720002 <= n:
        testSet.write(line)

mainSet.close()
testSet.close()
trainSet.close()
devSet.close()