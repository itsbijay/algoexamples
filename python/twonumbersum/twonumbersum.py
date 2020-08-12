# Two Number Sum

#  Write a function that takes in a non-empty array of distinct integers and an
#  integer representing a target sum.  If any two numbers in the input array
#  sum
#  up to the target sum, the function should return them in an array, in any
#  order.  If no two numbers sum up to the target sum, the function should
#  return
#  an empty array.
  
#  Note that the target sum has to be obtained by summing two different
#  integers
#  in the array; you can't add a single integer to itself in order to obtain
#  the
#  target sum.

# Sample Input
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Sample Output
# [-1, 11]
def twoNumberSum1(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []

def twoNumberSum2(array, targetSum):
    data = set()
    for i in range(len(array)):
        diff = targetSum - array[i]
        if array[i] in data:
            return [array[i], diff]
        data.add(diff)
    return []

print(twoNumberSum1([3, 5, -4, 8, 11, 1, -1, 6], 10))

print(twoNumberSum2([3, 5, -4, 8, 11, 1, -1, 6], 10))
