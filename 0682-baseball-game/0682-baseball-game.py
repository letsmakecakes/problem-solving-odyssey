class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        
        for op in operations:
            if op == '+':
                # Sum of last two scores (guaranteed to exist per problem constraints)
                records.append(records[-2] + records[-1])
            elif op == 'D':
                # Double the last score
                records.append(2 * records[-1])
            elif op == 'C':
                # Cancel the last score
                records.pop()
            else:
                # It's a number (positive or negative)
                records.append(int(op))
        
        return sum(records)

        