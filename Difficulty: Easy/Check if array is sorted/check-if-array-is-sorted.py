class Solution:
    def isSorted(self, arr) -> bool:
        """
        Check if an array is sorted in non-decreasing order.
        
        Args:
            arr: List of comparable elements
            
        Returns:
            True if array is sorted, False otherwise
            
        Examples:
            >>> isSorted([1, 2, 3, 4])
            True
            >>> isSorted([1, 3, 2])
            False
            >>> isSorted([1, 1, 2])
            True
        """
        # Handle edge cases
        if not arr or len(arr) <= 1:
            return True
            
        # Check each adjacent pair
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
            