class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        def r_contains(nums, size):
            if size == -1:
                return
            
            if size not in nums:
                return size
            
            return r_contains(nums, size - 1)
        
        return r_contains(nums, size)
            