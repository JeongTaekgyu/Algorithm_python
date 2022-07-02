def solution(s):
    answer = 0

    stack = []

    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
        else:
            if stack[len(stack)-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

    if len(stack) == 0:
        answer = 1

    return answer

s = 'cdcd'
print(solution(s))