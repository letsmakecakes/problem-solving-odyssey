class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Merge characters alternately from both strings
        merge_str = "".join(a + b for a, b in zip(word1, word2))
        # Add remaining characters from the longer string
        return merge_str + word1[len(word2):] + word2[len(word1):]