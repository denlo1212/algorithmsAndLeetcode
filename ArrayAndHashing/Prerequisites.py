from typing import List
# brute force solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplacationList = []

        for i in range(len(nums)):
            multiplacationNumber = 1
            for j, number in enumerate(nums):
                if i == j:  # Skip the current index
                    continue
                multiplacationNumber *= number
            multiplacationList.append(multiplacationNumber)
        return multiplacationList

solution = Solution()

nums = [1, 2, 3, 4]
result = solution.productExceptSelf(nums)
print(f"Input: {nums}")
print(f"Output: {result}")



# best solution
def productExceptSelf(self, nums: List[int]) -> List[int]:
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[1] = prefix
        prefix *= nums[i]
    postfix = 1

    for i in range(len(nums)-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result

nums = [1,2,4,6]
result = solution.productExceptSelf(nums)
print(f"Input: {nums}")
print(f"Output: {result}")