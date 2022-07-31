# def fibo(n):
#
#
# n = 20
# print(fibo(n))

def fibo(n):
    fib = [0, 1, 1]
    for i in range(3, n+1):
        fib.append((fib[i-2] + fib[i-1]) % 1234567)
    return fib[-1]  # 맨뒤에 있는거 반환

n = 10
print(fibo(n))
