class Solution:
    def numTrees(self, n: int) -> int:
        # Initialize DP aray with base cases
        dp = [0] * (n + 1)
        dp[0] = 1 # There's one BST with 0 nodes: the empty tree

        # Build the DP table
        for nodes in range(1, n + 1):
            for root in range(1, nodes + 1):
                left = root - 1 # Nodes in the left subtree
                right = nodes - root # Nodes in the right subtree
                dp[nodes] += dp[left] * dp[right]
        
        return dp[n]