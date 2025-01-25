class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Arrays of length 1 or 0 are always monotonic
        if len(nums) <= 2:
            return True

        # Initialize direction flag after checking first pair
        # 1 for increasing, -1 for decreasing, 0 for equal
        direction = 0

        # Find first non-equal pair to determine direction
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                direction = 1
                break
            elif nums[i] < nums[i - 1]:
                direction = -1
                break
        
        # If all elements were equal
        if direction == 0:
            return True
        
        # Check remaining elements follow the same direction
        for i in range(1, len(nums)):
            if direction == 1:
                if nums[i] < nums[i - 1]:
                    return False
            else:
                if nums[i] > nums[i - 1]:
                    return False
        
        return True