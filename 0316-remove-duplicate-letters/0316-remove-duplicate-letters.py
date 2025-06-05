class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Remove duplicate letters so that every letter appears exactly once.
        The result should be the smallest lexicographically among all possible results.

        Args:
            s: Input string containing lowercase letters
        
        Returns:
            String with duplicates removed in lexicographically smallest order
        
        Time Complexity: O(n) where n is length of string
        Space Complexity: O(1) since we have at most 26 unique characters
        """
        if len(s) <= 1:
            return s
        
        # Count frequency of each character
        char_count = Counter(s)
        
        # Tack characters already included in result
        used_chars = set()

        # Stack to build the lexicographically smallest result
        result_stack = []

        for char in s:
            # Decrease remaining count for current character
            char_count[char] -= 1

            # Skip if character already used
            if char in used_chars:
                continue
            
            # Remove larger characters from stack if:
            # 1. Current char is smallest than stack top
            # 2. Stack top character appears later in string
            while (result_stack and char < result_stack[-1] and char_count[result_stack[-1]] > 0):
                removed_char = result_stack.pop()
                used_chars.remove(removed_char)
            
            # Add current character to result
            result_stack.append(char)
            used_chars.add(char)
        
        return ''.join(result_stack)