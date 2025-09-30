class Solution:    
    def findUnion(self, a, b):
        """
        Find union of two arrays (removes duplicates).
        Time: O(n + m), Space: O(n + m)
        """
        # Create one set, update with other array
        result = set(a)
        result.update(b)
        return sorted(result)