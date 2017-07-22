testArray = [1, 2, 5, 3, 6, 7, 10, 100, 9]

def findMissing(numberList):
    i = 0
    missingNumber = []
    for x in numberList:
        arr.sort();
        i += 1
        while x != i:
            missingNumber.append(i)
            i+=1
    return missingNumber

print findMissing(testArray)
