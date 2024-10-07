from typing import List


class Solution:
    def hasDuplicate(self, numbers: List[int]) -> bool:
        existingNumbers = set()

        for number in numbers:
            if number in existingNumbers:
                return True
            existingNumbers.add(number)
        return False
