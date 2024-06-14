from stack import Stack


def reverse_string(str):
    stack = Stack()
    index = 0

    while index < len(str) and len(str) > 0:
        stack.push(str[index])
        index += 1

    if not stack.is_empty():
        rev_str = ""
        while not stack.is_empty():
            rev_str += stack.pop()
        return rev_str

    return ""


print(reverse_string("hello"))
