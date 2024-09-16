"""
This module implements a MaxHeap class, a data structure that maintains the largest element
at the root and allows efficient insertion and removal of the maximum element. 

The MaxHeap class supports basic heap operations such as insertion, deletion, and retrieval 
of the maximum element, as well as internal methods to maintain the heap property.
"""


class MaxHeap:
    """
    A MaxHeap is a binary heap data structure where the value of each parent node 
    is greater than or equal to the values of its children. The largest value is 
    always at the root of the heap.

    Attributes:
        heap (list): A list representation of the heap.
    """

    def __init__(self):
        """
        Initializes an empty MaxHeap.
        """
        self.heap = []

    def _left_child(self, index):
        """
        Returns the index of the left child of the given node.

        Args:
            index (int): The index of the parent node.

        Returns:
            int: The index of the left child.
        """
        return (2 * index) + 1

    def _right_child(self, index):
        """
        Returns the index of the right child of the given node.

        Args:
            index (int): The index of the parent node.

        Returns:
            int: The index of the right child.
        """
        return (2 * index) + 2

    def _parent(self, index):
        """
        Returns the index of the parent of the given node.

        Args:
            index (int): The index of the child node.

        Returns:
            int: The index of the parent node.
        """
        return (index - 1) // 2

    def _swap(self, index1, index2):
        """
        Swaps the values at the two given indices in the heap.

        Args:
            index1 (int): The index of the first element.
            index2 (int): The index of the second element.
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        """
        Inserts a new value into the heap, maintaining the max-heap property.

        Args:
            value: The value to be inserted into the heap.
        """
        self.heap.append(value)
        current = len(self.heap) - 1

        # Bubble up to maintain the heap property
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        """
        Ensures the heap property is maintained by sinking down an element if necessary.

        Args:
            index (int): The index of the element to sink down.
        """
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # Find the largest among the current node and its children
            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            # If the largest is not the current node, swap and continue sinking down
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        """
        Removes and returns the maximum value (the root) from the heap, maintaining 
        the heap property.

        Returns:
            The maximum value if the heap is not empty, None otherwise.
        """
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # Replace the root with the last element and sink down
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
