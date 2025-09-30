class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag algorithm (3-way partitioning).
        Sorts array of 0s, 1s, and 2s in-place in O(n) time, O(1) space.

        Invariants:
        - nums[0:low] contains all 0s
        - nums[low:mid] contains all 1s
        - nums[mid:high+1] contains unprocessed elements
        - nums[high+1:] contains all 2s
        """
        if not nums or len(nums) <= 1:
            return
        
        low = mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap with low boundary and advance both pointers
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                # Already in correct position
                mid += 1
            else: # nums[mid] == 2
                # Swap with high boundary, don't advance mid
                # (need to check the swapped element)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1