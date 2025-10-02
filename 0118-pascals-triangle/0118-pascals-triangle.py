class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generate Pascal's Triangle with the specified number of rows.
        Each row contains coefficients from binomial expansian.
        """
        if numRows == 0:
            return []

        triangle = [[1]]
        
        for row_num in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1]

            # Calculate middle values by summing adjacent elements from previous row
            for j in range(len(prev_row) - 1):
                new_row.append(prev_row[j] + prev_row[j + 1])

            new_row.append(1)
            triangle.append(new_row)
        
        return triangle