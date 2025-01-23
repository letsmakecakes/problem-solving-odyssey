class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_index = 0 # Index to place the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap non-zero element with the element at zero_index
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1