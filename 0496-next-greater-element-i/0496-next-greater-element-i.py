class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a dictionary to store next greater elements
        next_greater = {}

        # Create a stack to track elements
        stack = []

        # Process nums2 to find next greater elements
        for num in nums2:
            # While stack is not empty and current number is greater than top of stack
            while stack and stack[-1] < num:
                # Pop element and set its next greater element
                next_greater[stack.pop()] = num
            # Push current number to stack
            stack.append(num)
        
        # Create result array for nums1
        result = []

        # Fill result array using the dictionary
        for num in nums1:
            result.append(next_greater.get(num, -1))
        
        return result