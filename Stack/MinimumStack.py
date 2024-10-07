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


# Test case 1: Simple push and pop
min_stack = MinStack()
min_stack.push(2)
min_stack.push(1)
min_stack.push(3)
print(min_stack.getMin())  # Expected output: 1

min_stack.pop()
print(min_stack.getMin())  # Expected output: 1

min_stack.pop()
print(min_stack.getMin())  # Expected output: 2

# Test case 2: Push in descending order
min_stack.push(5)
min_stack.push(3)
min_stack.push(2)
print(min_stack.getMin())  # Expected output: 2

min_stack.pop()
print(min_stack.getMin())  # Expected output: 3

# Test case 3: Push in ascending order
min_stack.push(4)
min_stack.push(6)
min_stack.push(8)
print(min_stack.getMin())  # Expected output: 3

# Test case 4: Single element
min_stack = MinStack()
min_stack.push(10)
print(min_stack.getMin())  # Expected output: 10

min_stack.pop()
# Edge case: No elements after pop
try:
    print(min_stack.getMin())  # Should raise an exception or handle empty state
except IndexError:
    print("Stack is empty")

# Test case 5: Mixed push and pop
min_stack.push(7)
min_stack.push(1)
min_stack.push(5)
print(min_stack.getMin())  # Expected output: 1

min_stack.pop()
print(min_stack.getMin())  # Expected output: 1

min_stack.pop()
print(min_stack.getMin())  # Expected output: 7
