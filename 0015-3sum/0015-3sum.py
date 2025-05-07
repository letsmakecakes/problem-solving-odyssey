class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            # Skip duplicate values for the first position
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # If the smallest value is positive, no way to get sum of 0
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # Found a triplet
                    results.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers inward
                    left += 1
                    right -= 1

        return results