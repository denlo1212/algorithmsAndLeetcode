from typing import List

# my solution
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for currentDay, temperature in enumerate(temperatures):
            colderDays = 0
            for future_day in range(currentDay + 1, len(temperatures)):
                if temperatures[future_day] > temperature:
                    colderDays = future_day - currentDay
                    break
            result.append(colderDays)
        return result


# best solution
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair: [temperature, index]

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemperature, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append([temperature, index])
        return result


# Test case
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))
