class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted array in-place.
        
        Uses two-pointer technique to maintain unique elements at the start
        of the array while preserving their original order.
        
        Args:
            nums: Sorted list of integers (modified in-place)
            
        Returns:
            Number of unique elements (k), where first k elements are unique
            
        Examples:
            >>> nums = [1, 1, 2]
            >>> removeDuplicates(nums)
            2  # nums becomes [1, 2, _]
            
            >>> nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
            >>> removeDuplicates(nums)
            5  # nums becomes [0, 1, 2, 3, 4, _, _, _, _, _]
        """
        # Edge case: empty array
        if not nums:
            return 0
        
        # write_index points to position where next unique element should go
        write_index  = 0

        # Iterate through array starting from second element
        for read_index in range(1, len(nums)):
            # Found a new unique element
            if nums[read_index] != nums[write_index]:
                write_index += 1
                nums[write_index] = nums[read_index]
        
        # Return count of unique elements (index + 1)
        return write_index + 1