### Problem: [Validate Parentheses](https://neetcode.io/problems/validate-parentheses)
### Solution: stack
```python
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

```

### Problem: [Minimum Stack](https://neetcode.io/problems/string-encode-and-decode)
### Solution: stack
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

```

### Problem: [Evaluate Reverse Polish Notation](https://neetcode.io/problems/string-encode-and-decode)
### Solution: stack
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+", "-", "*", "/")
        values = []

        for token in tokens:

            if token not in operators:
                print(token)
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
```

### Problem: []()
### Solution: stack
```python

```

### Problem: [Daily Temperatures](https://neetcode.io/problems/string-encode-and-decode)
### Solution: stack
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # pair: [temperature, index]

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemperature, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append([temperature, index])
        return result

```

### Problem: [Car Fleet](https://neetcode.io/problems/car-fleet)
### Solution: stack
```python
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

```

### Problem: []()
### Solution: stack
```python

```

### Problem: []()
### Solution: 
```python

```
