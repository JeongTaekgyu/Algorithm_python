def solution(x, n):
    answer = []

    for i in range(1, n+1):
        answer.append(x * i)

    return answer

x = -3
n = 5
print(solution(x, n))