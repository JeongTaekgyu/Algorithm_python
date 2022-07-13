input = 20


def fibo_recursion(n):
    # 구현해보세요!
    if n == 2 or n == 1:
        return 1

    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # input = 20, 6765

# 1 1 2 3 5 8 13 21
# 1. fibo(3) = fibo(2) + fibo(1)
# 2. fibo(4) = fibo(3) + fibo(2)
# 3. fibo(5) = fibo(4) + fibo(3)
# 반복하지 않으려면 동적계획법을 사용해야한다.
