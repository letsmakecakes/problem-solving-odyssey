class Solution:
    def celebrity(self, mat):
        """
        Find the celebrity in the party using the elimination approach.
        
        Args:
            matrix (List[List[int]]): n x n matrix where matrix[i][j] represents if person i knows person j
            
        Returns:
            int: Index of celebrity if found, -1 otherwise
        """
        n = len(mat)
        if n == 0:
            return -1
        
        # Find potential celebrity using elemination
        potential_celebrity = self._find_potential_celebrity(mat)
        
        # Verify if the potential celebrity is actually a celebrity
        if potential_celebrity != -1:
            return potential_celebrity if self._verify_celebrity(mat, potential_celebrity) else -1
        
        return -1
    
    def _find_potential_celebrity(self, matrix: list[list[int]]) -> int:
        """
        Find a potential celebrity using two-pointer approach.
        
        Args:
            matrix (List[List[int]]): The relationship matrix
        
        Returns:
            int: Index of potential celebrity, or -1 if not found
        """
        left = 0
        right = len(matrix) - 1
        
        while left < right:
            if matrix[left][right]: # If left knows right
                left += 1
            elif matrix[right][left]: # If right knows left
                right -= 1
            else:   # Neither knows each other
                left += 1
                right -= 1
        
        return left if left <= right else -1
    
    def _verify_celebrity(self, matrix: list[list[int]], candidate: int) -> bool:
        """
        Verify if the candidate is actually a celebrity.
        
        Args:
            matrix (List[List[int]]): The relationship matrix
            candidate (int): Index of potential celebrity
        
        Returns:
            bool: True if candidate is celebrity, False otherwise
        """
        n = len(matrix)
        
        for i in range(n):
            if i == candidate:
                continue
            # Check if candidate knows anyone or someone doesn't know candidate
            if matrix[candidate][i] == 1 or matrix[i][candidate] == 0:
                return False
        
        return True
#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))
        print("~")

# } Driver Code Ends