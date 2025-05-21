class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_index = {} # Dictionary to store character -> index mapping
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            # If character is already in current window, move start pointer
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            else:
                # Update max_length if current window is larger
                max_length = max(max_length, end - start + 1)
        
            # Update character index
            char_index[char] = end

        return max_length