# Convert decimal integer to binary

from stack import Stack


def decimal_to_binary(stack, input_decimal):
    while input_decimal > 0:
        stack.push(input_decimal % 2)
        input_decimal //= 2
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    return binary


stack = Stack()
input_decimal = 242
print(decimal_to_binary(stack, input_decimal))