class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates in-place from a sorted array and return the number of unqiue elements..

        Args:
            nums: A sorted array of integers
        
        Returns:
            The number of unique elements in the array
        """
        # Handle empty array case
        if not nums:
            return 0
        
        # Use two-pointer technique to track unique elements
        # left pointer keeps trck of the position for the next unique element
        unique_position = 0

        # Iterate through the array starting from the second element
        for current in range(1, len(nums)):
            # When we find a new unique element
            if nums[current] != nums[unique_position]:
                # Move unique_position forward
                unique_position += 1
                # Place the new unique element at the next position in our result
                nums[unique_position] = nums[current]
        
        # unique_position is zero-indexed, so add 1 to get the count
        return unique_position + 1