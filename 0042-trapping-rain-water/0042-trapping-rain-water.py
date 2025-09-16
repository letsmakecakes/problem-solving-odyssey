class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate trapped rainwater using two-pointer approach.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            height: List of non-negative integers representing elevation map
            
        Returns:
            Total units of water that can be trapped
        """
        if not height or len(height) < 3:
            return 0
        
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        trapped_water = 0

        while left < right:
            # Process the side with smaller height
            if height[left] <= height[right]:
                trapped_water += self._process_left_side(height, left, left_max)
                left_max = max(left_max, height[left])
                left += 1
            else:
                trapped_water += self._process_right_side(height, right, right_max)
                right_max = max(right_max, height[right])
                right -= 1
        
        return trapped_water
    
    def _process_left_side(self, height: List[int], left: int, left_max: int) -> int:
        """Calculate water trapped at left position."""
        return max(0, left_max - height[left])
    
    def _process_right_side(self, height: List[int], right: int, right_max: int) -> int:
        """Calculate water trapped at right position."""
        return max(0, right_max - height[right])