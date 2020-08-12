
#  Given two non-empty arrays of integers, write a function that determines
#  whether the second array is a subsequence of the first one.

#  A subsequence of an array is a set of numbers that aren't necessarily adjacent
#  in the array but that are in the same order as they appear in the array. For
#  instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. 
#  Note that a single number in an array and the array itself are both valid subsequences of the array.
  
#  Sample Input  = [5, 1, 22, 25, 6, -1, 8, 10]
#  sequence = [1, 6, -1, 10]
  
#  Sample Output
#  true

#[1] [2,3,4,1]: true
#[1] [2,3,4,0]: false
#[3] [2,3]: false

#[2,1] [2,3,0,9,1]: true


def validateSubsequence1(array, sequence):
    seqIdx = 0
    for item in array:
        if item == sequence[seqIdx]:
            seqIdx = seqIdx + 1
    return seqIdx == len(sequence)


def validateSubsequence2(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx = seqIdx + 1
        arrIdx = arrIdx + 1
    return seqIdx == len(sequence)

print(validateSubsequence1([2,3,0,9,1], [0, 1]))

print(validateSubsequence2([2,3,0,9,1], [0, 1]))