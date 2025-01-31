class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        # Rotate the queue to maintain stack order
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        Removes and returns the element on top of the stack.
        """
        if not self.empty():
            return self.queue.popleft()
        raise IndexError("pop from an empty stack")

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.empty():
            return self.queue[0]
        raise IndexError("peek at empty stack")

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()