class Solution:
    def reverse(self, s: str) -> str:
        if not s:
            return ""
        
        stack = list(s)  # directly initialize stack with characters
        return ''.join(stack.pop() for _ in range(len(stack)))