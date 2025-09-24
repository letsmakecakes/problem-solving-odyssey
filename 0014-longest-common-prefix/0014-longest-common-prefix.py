class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix string amongst an array of strings.

        Time Complexity: O(S) where s is sum of all characters in all strings
        Space Complexity: O(1) - only using variables for indexing

        Args:
            strs: List of strings to find common prefix from

        Returns:
            The longest common prefix string, empty string if no common prefix
        """
        if not strs:
            return ""
        
        # Handle single string case
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        for s in strs[1:]:
            while prefix and not s.startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix
            