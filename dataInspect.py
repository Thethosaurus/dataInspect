arr = [1, 2, 5, 3, 6, 7, 10, 100, 9]
#missingNumber = []

def findMissing(stuff):
    i = 0
    missingNumber = []
    for x in stuff:
        arr.sort();
        i += 1
        while x != i:
            # print i
            # print x
            # for a in range (arr[i-1], arr[i]):
                # numberRange = arr[i-1]
            missingNumber.append(i)
                # numberRange += 1
            # arr.append(missingNumber[a])
            # arr.sort()
            # print arr

            i+=1
    return missingNumber

print findMissing(arr)

# arr = [1, 2, 3, 5, 6, 7, 9 ,10]
# #missingNumber = []
#
# def findMissing(stuff):
#     i = 0
#     missingNumber = []
#     for x in stuff:
#         i += 1
#         print i
#         if x != i:
#             missingNumber.append(i)
#             i -= 1
#     return missingNumber
#
# print findMissing(arr)
