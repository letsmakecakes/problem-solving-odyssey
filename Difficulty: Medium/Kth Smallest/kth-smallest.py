#User function Template for python3
import heapq

class Solution:
    def kthSmallest(self, arr,k):
        """
        Find the kth smallest element in an array using a min heap.
        
        Args:
            arr: List of integers
            k: Position of smallest element to find (1-indexed)
        
        Returns:
            The kth smallest element, or None if invalid input
        """
        # Validate input
        if not arr or k <= 0 or k > len(arr):
            return None
        
        # Maintain a min heap
        min_heap = []
        for num in arr:
            heapq.heappush(min_heap, num)
            
         # Pop k-1 times to reach kth smallest
        for _ in range(k - 1):
            heapq.heappop(min_heap)
            
        
        return heapq.heappop(min_heap)
