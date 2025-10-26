def balancedParens(text: str) -> bool:
    stack = []
    openers = "([{"
    closers = ")]}"
    matches = {")": "(", "]": "[", "}": "{"}

    for char in text:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()

    return len(stack) == 0

text = "({[()]})"
print(balancedParens(text))  # Output: True

