class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]

        # Compare from both ends
        left, right = 0, len(filtered_chars) - 1
        while left < right:
            if filtered_chars[left] != filtered_chars[right]:
                return False
            left += 1
            right -= 1
        
        return True