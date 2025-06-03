class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Find the duplicate number in an array whwre each element appears once or twice.

        Args:
            nums: List of integers where one number appears twice
        
        Returns:
            The duplicate number, or -1 if no duplicate found
        """
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
        return -1