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

    elif  0 < n < 630001:
        trainSet.write(line)
    
    elif 630001 <= n:
        devSet.write(line)
    
    n += 1

mainSet.close()
testSet.close()
trainSet.close()
devSet.close()