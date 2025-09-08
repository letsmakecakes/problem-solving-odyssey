class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Find the duplicate number in an array using Floyd's Cycle Detection Algorithm.
        
        Given an array of integers nums containing n + 1 integers where each integer 
        is in the range [1, n] inclusive, there is only one repeated number.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: List of integers with exactly one duplicate
            
        Returns:
            The duplicate integer
        """
        # Phase 1: Detect if cycle exists using Floyd's algorithm
        slow_pointer = self._get_next(nums, nums[0])
        fast_pointer = self._get_next(nums, self._get_next(nums, nums[0]))

        while slow_pointer != fast_pointer:
            slow_pointer = self._get_next(nums, slow_pointer)
            fast_pointer = self._get_next(nums, self._get_next(nums, fast_pointer))
        
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        finder = nums[0]
        while finder != slow_pointer:
            finder = self._get_next(nums, finder)
            slow_pointer = self._get_next(nums, slow_pointer)
        
        return finder
    
    def _get_next(self, nums: List[int], current: int) -> int:
        """
        Helper method to get the next position in the cycle.
        Treats the array as a linked list where nums[i] points to index nums[i].
        """
        return nums[current]