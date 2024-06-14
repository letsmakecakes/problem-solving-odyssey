from stack import Stack


def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    return False


def is_balanced(expression):
    stack = Stack()
    index = 0
    is_balanced_cond = True

    while index < len(expression) and is_balanced_cond:
        paren = expression[index]

        if paren in "([{":
            stack.push(paren)
        else:
            if stack.is_empty():
                is_balanced_cond = False
                break
            else:
                top = stack.pop()
                if not is_match(top, paren):
                    is_balanced_cond = False
                    break
        index += 1

    if stack.is_empty() and is_balanced_cond:
        return True

    return False


expression = "[()]{}{[()()]()}"
print(is_balanced(expression))
