from math import ceil

class Solution:
    def mergeArrays(self, a, b):
        """
        Merge two sorted arrays in-place using shell sort gap sequence.
        
        Args:
            a: First sorted array (modified in-place)
            b: Second sorted array (modified in-place)
        """
        n, m = len(a), len(b)
        total_len = n + m
        gap = ceil((total_len) /  2)
        
        while gap > 0:
            self._compare_and_swap_with_gap(a, b, n, total_len, gap)
            gap = self._next_gap(gap)
    
    def _compare_and_swap_with_gap(self, a, b, n, total_len, gap):
        """Compare and swap elements with given gap distance."""
        for i in range(total_len - gap):
            j = i + gap
            
            left_val = self._get_element(a, b, n, i)
            right_val = self._get_element(a, b, n, j)
            
            if left_val > right_val:
                self._set_element(a, b, n, i, right_val)
                self._set_element(a, b, n, j, left_val)
    
    def _get_element(self, a, b, n, index):
        """Get element at virtual index combined arrays."""
        return a[index] if index < n else b[index - n]
    
    def _set_element(self, a, b, n, index, value):
        """Set element at virtual index in combined arrays."""
        if index < n:
            a[index] = value
        else:
            b[index - n] = value
    
    def _next_gap(self, gap):
        """Calculate next gap in sequence."""
        return gap // 2 if gap == 1 else ceil(gap / 2)