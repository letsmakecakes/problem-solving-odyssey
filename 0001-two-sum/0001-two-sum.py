class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to the target.

        Args:
            nums: List of integers to search
            target: Target sum to find
        
        Returns:
            List containing indices of the numbers that sum to target.
            Returns empty list if no solution exists.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = {}

        for idx, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], idx]

            seen[num] = idx

        return []     