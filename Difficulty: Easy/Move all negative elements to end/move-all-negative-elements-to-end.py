#User function Template for python3

class Solution:
    def segregateElements(self, arr):
        """
        Segregate positive and negative numbers (single pass, optimized).
        Time: O(n), Space: O(n)
        """
        n = len(arr)
        result = []
        
        # Single pass: collect positives first
        for x in arr:
            if x >= 0:
                result.append(x)
        
        # Single pass: collect negatives
        for x in arr:
            if x < 0:
                result.append(x)
        
        # Copy back to original array
        for i in range(n):
            arr[i] = result[i]
