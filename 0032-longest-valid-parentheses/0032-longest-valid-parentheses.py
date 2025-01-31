class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize stack with -1 to handle edge cases
        stack = [-1]
        max_length = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                # Push index of opening parenthesis
                stack.append(i)
            else:
                # Pop the last opening parenthesis or sentinel value
                stack.pop()

                if not stack:
                    # Push current index as new sentinel
                    stack.append(i)
                else:
                    # Calculate length of valid substring'
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)
        
        return max_length