x = input()
def split(word):
    return [char for char in word]
aList = split(x)
def longest_run(aList):

    maxCount = 1
    actualCount = 1

    for i in range(len(aList)-1):
        if aList[i] == aList[i+1]:
            actualCount += 1
        else:
            actualCount = 1
        if actualCount > maxCount:
            maxCount = actualCount

    print(maxCount)

longest_run(aList)
