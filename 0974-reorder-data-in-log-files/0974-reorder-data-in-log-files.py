class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        Single-pass solution using Python's stable sort.
        Time: O(n log n), Space: O(1) auxiliary
        """
        def sort_key(log: str) -> tuple:
            space_idx = log.find(' ')
            content = log[space_idx + 1:]
            identifier = log[:space_idx]

            # Digit logs: sort by original order (stable sort handles this)
            # Letter logs: sort by (content, identifier)
            if content[0].isdigit():
                return (1, 0, 0) # All digit log get the same key, preserving order
            return (0, content, identifier) # Letter logs sort by content, then ID
        
        return sorted(logs, key=sort_key)
    
    