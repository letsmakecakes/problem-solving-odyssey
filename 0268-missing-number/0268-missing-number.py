class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Calculate expected sum of numbers from 0 to n
        n = len(nums)
        expected_sum = n * (n + 1) // 2

        # Calculate actual sum of elements in nums
        actual_sum = sum(nums)

        # The difference is the missing number
        return expected_sum - actual_sum