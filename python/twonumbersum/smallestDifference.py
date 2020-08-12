
#  Write a function that takes in two non-empty arrays of integers, finds the
#  pair of numbers (one from each array) whose absolute difference is closest to
#  zero, and returns an array containing these two numbers, with the number from
#  the first array in the first position.

#  You can assume that there will only be one pair of numbers with the smallest difference.

# arraryOne:  = [-1, 5, 10, 20, 28, 3]
# arraryTwo = [26, 134, 135, 15, 17]

# Sample Output: [28, 26]

def smallestDifference(arrayOne, arrayTwo):
    firstIndx = 0
    secondIndx = 0
    arrayOne.sort()
    arrayTwo.sort()
    pair = []
    smallest = 0

    while firstIndx < len(arrayOne) and secondIndx < len(arrayTwo):
        current = 0
        temp = arrayOne[firstIndx] - arrayTwo[secondIndx]
        diff = temp * -1 if temp < 0 else temp
        smallest = current if firstIndx == 0 else smallest

        current = diff if diff < smallest else smallest

        if smallest < current:
            smallest = [arrayOne[firstIndx], arrayTwo[secondIndx]]

        firstIndx = firstIndx + 1
        secondIndx = secondIndx + 1

    return pair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))