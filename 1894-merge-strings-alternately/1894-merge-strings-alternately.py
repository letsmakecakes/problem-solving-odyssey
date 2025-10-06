class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merges two strings by alternating characters from each string.

        Args:
            word1: First string
            word2: Second string
        
        Returns:
            Merged string with alternating characters
        
        Time Complexity: O(n + m) where n, m are lengths of word1, word2
        Space Complexity: O(n + m) for the result string
        """
        result = []
        min_len = min(len(word1), len(word2))

        # Alternate characters from both strings
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])
        
        # Append remaining characters from the longer string
        result.append(word1[min_len:])
        result.append(word2[min_len:])

        return ''.join(result)