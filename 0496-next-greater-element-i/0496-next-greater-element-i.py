class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Build next greater element mapping for nums2
        next_greater = self._build_next_greater_map(nums2)

        # Map results for nums1
        return [next_greater.get(num, -1) for num in nums1]

        
    def _build_next_greater_map(self, nums: List[int]) -> dict[int, int]:
        """
        Build a mapping of each number to its next greater element using a monotonic stack.

        Args:
            nums: Array of numbers to process
        
        Returns:
            Dictionary mapping eachg number to its next greater element
        """
        next_greater = {}
        stack = []

        for num in nums:
            # Pop all smaller elements and set current num as their next greater
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            
            stack.append(num)

        return next_greater