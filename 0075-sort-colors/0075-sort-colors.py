class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort array containing only 0s, 1s, and 2s in-place using Dutch National Flag algorithm.
        Time: O(n), Space: O(1)
        """
        # Define color constants for better readability
        RED, WHITE, BLUE = 0, 1, 2
        
        # Pointers: left tracks position for next 0, right tracks position for next 2
        left, current, right = 0, 0, len(nums) - 1
        
        while current <= right:
            if nums[current] == RED:
                # Move red (0) to the left section
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == WHITE:
                # White (1) is already in correct section, just move forward
                current += 1
            else:  # nums[current] == BLUE
                # Move blue (2) to the right section
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
                # Don't increment current - need to check swapped element