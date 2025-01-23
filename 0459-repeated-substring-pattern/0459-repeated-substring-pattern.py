class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, (n // 2) + 1): # Only consider substrings up to half the length of s
            if n % i == 0:  # The length of s must be a multiple of the substring's length
                substring = s[:i] 
                if substring * (n // i) == s: # Check if the repeating substring forms s
                    return True
        
        return False