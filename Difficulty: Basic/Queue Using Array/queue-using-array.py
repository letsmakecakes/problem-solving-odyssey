from collections import deque

class myQueue:
    """A fixed-size queue implementation with O(1) dequeue operations."""
    
    def __init__(self, n):
        """
        Initialize a queue with a fixed capacity.
        
        Args:
            n: Maximum number of elements the queue can hold
        """
        self._queue = deque()
        self._capacity = n
    
    def isEmpty(self):
        """Check if the queue is empty/"""
        return len(self._queue) == 0
    
    def isFull(self):
        """Check if the queue has reached its capacity."""
        return len(self._queue) == self._capacity

    def enqueue(self, x):
        """
        Add an item to the rear of the queue.
        
        Args:
            x: The item to add
        
        Returns:
            True if successful, False if queue is full
        """
        if self.isFull():
            return False
        self._queue.append(x)
        return True

    def dequeue(self):
        """
        Remove and return the front item from the queue.
        
        Returns:
            The front item, or None if queue is empty
        """
        if self.isEmpty():
            return None
        return self._queue.popleft()

    def getFront(self):
        """
        Get the front item without removing it.
        
        Returns:
            The front item, or None if queue is empty
        """
        return self._queue[0] if not self.isEmpty() else -1
        
    def getRear(self):
        """
        Get the rear item without removing it.
        
        Returns:
            The rear item, or None if queue is empty
        """
        return self._queue[-1] if not self.isEmpty() else -1
        