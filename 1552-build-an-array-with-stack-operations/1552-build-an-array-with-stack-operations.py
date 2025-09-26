class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        Build an array using stack operations to match the target array.

        Args:
            target: List of integers to build (assumed to be stored and within [1, n])
            n: Upper bound for the stream of integers [1, 2, ..., n]

        Returns:
            List of stack operations ("Push" or "Pop") to build the target array
        """
        if not target:
            return []
        
        operations = []
        current_stream_value = 1
        
        for target_value in target:
            # For each number we need to skip, push then pop
            while current_stream_value < target_value:
                operations.extend(["Push", "Pop"])
                current_stream_value += 1
            
            # Push the target value (no pop needed as we want to keep it)
            operations.append("Push")
            current_stream_value += 1
        
        return operations