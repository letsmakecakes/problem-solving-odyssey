class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
        You must do it in place.
        
        Uses first row and column as markers for zero positions.

        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # Check if first row or column contains zero
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
                    
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
    
        # Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set zeros based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle first row
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # Handle first column
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
