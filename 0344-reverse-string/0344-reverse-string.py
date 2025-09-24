class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse a list of characters in-place using two pointers.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            s: List of single characters to reverse in-place
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        