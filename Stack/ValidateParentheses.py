class Solution:
    def isValid(self, string: str) -> bool:
        closedBrackets = {")": "(", "]": "[", "}": "{"}
        stack = []

        for character in string:
            if character not in closedBrackets:
                stack.append(character)

            else:
                # check if the list is not empty then check if the opening bracket matches the closing bracket
                if not stack or stack[-1] != closedBrackets[character]:
                    return False
                stack.pop()


        return not stack




# Create an instance of the Solution class
solution = Solution()


# Test case 1: Nested brackets
print(solution.isValid("(())"))  # Expected output: True

# Test case 2: Mixed nested brackets
print(solution.isValid("{[()]}"))  # Expected output: True


# Test case 3: Unbalanced brackets (mismatched brackets)
print(solution.isValid("([)]"))  # Expected output: False


