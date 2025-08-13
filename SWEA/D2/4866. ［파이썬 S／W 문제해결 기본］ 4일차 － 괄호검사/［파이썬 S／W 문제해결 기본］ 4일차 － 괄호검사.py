T = int(input())

for test_case in range(1, T + 1):
    words = input()
    stack = []
    result = 1

    for word in words:
        if word == '{':
            stack.append(word)
        elif word == '(':
            stack.append(word)
        elif word == '}':
            if len(stack) == 0:
                result = 0
            elif stack.pop() != '{':
                result = 0
        elif word == ')':
            if len(stack) == 0:
                result = 0
            elif stack.pop() != '(':
                result = 0

    if len(stack) > 0:
        result = 0

    print(f"#{test_case} {result}")