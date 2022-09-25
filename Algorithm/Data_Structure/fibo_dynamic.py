input = 100

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1,
}

# 1. 만약 메모에 그 값이 있다면 바로 반환한다.
# 2. 피보나치 값을 처음 구했다면 메모에 그 값을 기록한다.

# 100 -> 1 로 가는 Top Down 방식이다. 반대로하면 Bottom Up 방식이다.
def fibo_dynamic_programming(n, fibo_memo):
    # 1. 만약 메모에 그 값이 있다면 바로 반환한다.
    if n in fibo_memo:
        return fibo_memo[n]

    # 2. 피보나치 값을 처음 구했다면 메모에 그 값을 기록한다.
    # 없으면 n번째 fibo 값을 구해라
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)

    # 구한 값을 메모에 기록한다.
    fibo_memo[n] = nth_fibo
    return nth_fibo


print(fibo_dynamic_programming(input, memo))