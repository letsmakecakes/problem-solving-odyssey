class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing whitespace and work backwards
        s = s.rstrip()
        
        # Handle empty string after stripping
        if not s:
            return 0

        # Count characters from the end until we hit a space
        length = 0
        for char in reversed(s):
            if char == ' ':
                break
            length += 1

        return length