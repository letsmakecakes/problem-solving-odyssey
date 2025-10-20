class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 1):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early termination: if smallest number is positive, no solution possible
            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]

                if three_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicate values for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result 