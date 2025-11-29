class Solution:
    def secondHighest(self, s: str) -> int:
        digits = {int(ch) for ch in s if ch.isdigit()}

        if len(digits) < 2:
            return -1
        
        sorted_digits = sorted(digits, reverse=True)
        return sorted_digits[1]