class MinStack:
    def __init__(self):
        """Initialize two empty stacks: main stack and min stack."""
        self.stack = [] # Main stack to store values
        self.min_stack = [] # Auxiliary stack to track minimums

    def push(self, val: int) -> None:
        """
        Push element onto stack and update minimum stack.
        Time complexity: O(1)

        Args:
            val: Integer value to push onto stack
        """
        self.stack.append(val)

        # Update min_stack - if empty or val is smaller/equal to current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Remove element from top of stack
        Time complexity: O(1)
        """
        if self.stack:
            # If popping minimum value, remove from min_stack too
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        """
        Get top element of stack.
        Time Complexity: O(1)

        Returns:
            int: Top element of stack
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Get minimum element in stack.
        Time complexity: O(1)

        Returns:
            int: Minimum element in stack
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()