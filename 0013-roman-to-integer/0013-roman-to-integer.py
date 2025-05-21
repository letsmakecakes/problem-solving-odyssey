class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
            
        roman_map = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        
        result = 0
        prev_value = 0

        # Process from right to left
        for char in reversed(s):
            current_value = roman_map[char]

            # If current value is greater than or equal to previous, add it
            # Otherwise subtract it (handles cases like IV, IX, etc.)
            if current_value >= prev_value:
                result += current_value
            else:
                result -= current_value
            
            prev_value = current_value
        
        return result