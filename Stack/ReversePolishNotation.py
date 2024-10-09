from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+", "-", "*", "/")
        values = []

        for token in tokens:

            if token not in operators:
                values.append(int(token))
            else:
                b = values.pop()  # Pop the second operand
                a = values.pop()  # Pop the first operand

                if token == "+":
                    values.append(a + b)
                elif token == "-":
                    values.append(a - b)
                elif token == "*":
                    values.append(a * b)
                elif token == "/":
                    values.append(int(a / b))

        return values[0]
# Test case
tokens = ["2", "1", "+", "3", "*"]
solution = Solution()
result = solution.evalRPN(tokens)
print(result)  # Expected output: 9
