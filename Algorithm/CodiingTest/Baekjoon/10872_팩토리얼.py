import sys

n = int(input())
#n = int(sys.stdin.readline())

# 재귀 아닌 방법
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#
#     return result

# 재귀 방법
def factorial(n):
    if n == 0:
        return 1

    n *= factorial(n-1)

    return n

print(factorial(n))