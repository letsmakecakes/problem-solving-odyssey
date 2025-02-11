class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Converts a list of integers into the largest possible number by concatenating them.

        Args:
            nums: List[int] - List of non-negative integers
        
        Returns:
            str - The largest possible number formed by concatenating the input integers
        
        Example:
            Input: nums = [10, 2]
            Output: "210"
        """
        # Custom comparison function for sorting
        def compare(x: str, y: str) -> int:
            return 1 if x + y < y + x else -1 if x + y > y + x else 0
        
        # Convert numbers to strings for easier comparison
        str_nums = [str(num) for num in nums]

        # Sort using custom comparison
        str_nums.sort(key=cmp_to_key(compare))
        
        # Handle edge cases where the largest number is 0
        if str_nums[0] == '0':
            return '0'
        
        # Join the sorted strings to form the result
        return ''.join(str_nums)