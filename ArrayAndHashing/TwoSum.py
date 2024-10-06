from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : index

        for index, number in enumerate(nums):
            difference = target - number
            if difference in prevMap:
                return [prevMap[difference], index]
            prevMap[number] = index



# Test cases
solution = Solution()

# Test Case 1: Basic test with positive numbers
print(solution.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]

# Test Case 2: Negative numbers
print(solution.twoSum([-3, 4, 3, 90], 0))  # Expected: [0, 2]