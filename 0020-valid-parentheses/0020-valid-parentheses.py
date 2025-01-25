class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if string has valid parentheses/bracket/brace pairs.

        Args:
            s (str): String containing parentheses/brackets/braces
        
        Returns:
            bool: True if all pairs are valid and properly nested, False otherwise
        """
        # Dictionary mapping closing brackets to their corresponding opening brackets
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            # If it's an opening bracket, add to stack
            if char not in brackets:
                stack.append(char)
            # If it's a closing bracket
            else:
                # Check if stack is empty or if brackets don't match
                if not stack or stack.pop() != brackets[char]:
                    return False
        
        # String is valid only if stack is empty
        return len(stack) == 0