class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find the indices of two numbers in a sorted array that add up to the target.

        Args:
            numbers: A sorted list of integers
            target: The target sum
        
        Returns:
            A list containing the 1-indexed positions of the two numbers that add up to the target, or an empty list if no solution exists.
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Return 1-indexed positions as per problem requirements
                return [left+1, right+1]
            
            # Move pointers based on comparison with target
            if current_sum > target:
                right -= 1
            else: # current_sum > target
                left += 1
        
        # No solution found
        return []