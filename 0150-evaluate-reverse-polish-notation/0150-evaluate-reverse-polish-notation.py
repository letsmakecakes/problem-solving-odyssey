class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Define a dictionary of operations for cleaner, more extensible code
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            "*": lambda x, y: x * y,
            '/': lambda x, y: int(x / y) # Use int() for truncation towards zero
        }

        # Use a stack to track numeric values
        stack = []

        for token in tokens:
            # If token is an operator, perform the calculation
            if token in operations:
                # Pop the two most recent numbers (note the order matters)
                num2 = stack.pop()
                num1 = stack.pop()

                # Apply the corresponding operation and push the result back to stack
                result = operations[token](num1, num2)
                stack.append(result)
            else:
                # If not an operator, convert to integer and push to stack
                stack.append(int(token))
        
        # Return the final result (top of the stack)
        return stack[-1]