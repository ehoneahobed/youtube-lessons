#!/usr/bin/python3
'''Solution to the 2 sum problem'''

def twosum(nums, target):
    # outer loop to get each member
    for i in range(len(nums)):
        # inner loop that enables the subsequent additions
        for j in range(i + 1, len(nums)):
            mysum = nums[i] + nums[j]
            if mysum == target:
                return (i, j)


def twosumsPro(nums, target):
    for i in range(len(nums)):
        expectedValue = target - nums[i]
        # check if the expected value exists in the list
        try:
            expectedIndex = nums.index(expectedValue, i +1)
            return (i, expectedIndex)
        except ValueError:
            continue


nums = [4, 5, 1, 3] # (0, 1)
target = 8
print(twosum(nums, target))

print()

print(twosumsPro(nums, target))