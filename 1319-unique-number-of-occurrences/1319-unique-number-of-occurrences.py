class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Check if the number of occurences of each value in the array is unique.

        Args:
            arr: List of integers
        
        Returns:
            True if all occurence counts are unique, False otherwise
        """
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        
        occurrences = list(counts.values())
        return len(occurrences) == len(set(occurrences))