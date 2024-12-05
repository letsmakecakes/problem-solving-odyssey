class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == 0:
                    result.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return list(result)