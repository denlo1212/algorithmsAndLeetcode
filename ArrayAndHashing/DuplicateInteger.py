from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # in a hashSet you can not get a duplicate
        hashSet = set()
        for number in nums:
            if number in hashSet:
                return True
            hashSet.add(number)
        return False



solution = Solution()
result = solution.hasDuplicate([1, 2, 3, 3])
print(result)
