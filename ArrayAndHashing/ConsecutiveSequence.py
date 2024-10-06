from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set(nums)
        highestStreak = 0

        # looping trough the set is faster then the array because of duplicates
        for number in numberSet:
            if (number - 1) not in numberSet:
                streak = 1
                while (number + streak) in numberSet:
                    streak += 1
                highestStreak = max(streak, highestStreak)
        return highestStreak


solution = Solution()
result = solution.longestConsecutive([2, 20, 4, 10, 3, 4, 5])
print(result)