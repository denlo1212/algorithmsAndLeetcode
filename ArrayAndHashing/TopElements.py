from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequentie = [[] for i in range(len(nums) + 1)]  # bucket sort

        for number in nums:
            count[number] = 1 + count.get(number, 0)

        for number, counter in count.items():
            frequentie[counter].append(number)

        result = []
        for index in range(len(frequentie) - 1, 0, -1):
            for number in frequentie[index]:
                result.append(number)
                if len(result) == k:
                    return result


solution = Solution()
anagrams = solution.topKFrequent([7, 7, 7, 9, 2, 4, 5], 2)
print(anagrams)
