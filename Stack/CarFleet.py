from typing import List


class Solution:
    def carFleet(self, target: int, positions: List[int], speed: List[int]) -> int:
        pair = list(zip(positions, speed))
        pair.sort(reverse=True)
        stack = []

        for position, speed in pair:
            stack.append((target - position)/ speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



solution = Solution()

target = 12
positions = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

print(solution.carFleet(target, positions, speed))
