class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort an array of 0s, 1s, and 2s in-place using the Dutch National Flag algorithm.
        This is also known as the 3-way partitioning problem.

        Args:
            nums: List[int] - Array containing only 0s, 1s, and 2s
        
        Modifies the input array in-place.

        Time Complexity: O(n) - single pass algorithm
        Space Complexity: O(1) - constant extra space
        """
        # Edge case: array with 0 or 1 element
        if len(nums) <= 1:
            return
        
        # Initialize pointers
        left = 0                # pointer for 0s (left section)
        current = 0             # current element being examined
        right = len(nums) - 1   # pointer for 2s (right section)

        while current <= right:
            if nums[current] == 0:
                # Swap current element with left pointer
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                # Swap the current element with right pointer
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
            else: # nums[current] == 1
                # 1s stay in the middle section
                current += 1