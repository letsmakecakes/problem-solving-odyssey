class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        # Mapping of closing to opening brackets
        matching = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # Check if character is a valid bracket
            if char not in matching and char not in matching.values():
                return False
            
            # If it's an opening bracket, push to stack
            if char in matching.values():
                stack.append(char)
            # If it's a closing bracket
            else:
                # Check if stack is empty or top doesn't match
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
        
        # Valid if stack is empty
        return len(stack) == 0