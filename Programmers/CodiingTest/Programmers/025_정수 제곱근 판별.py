import math

def solution(n):

    # 파이썬에서는 long형을 따로 두지 않고 모든 정수는 int형 하나로 표시한다.
    tmp = int(math.sqrt(n))

    if math.sqrt(n) - tmp == 0:
        return (tmp+1) ** 2 # n ** m 이면 n의 m제곱
    else:
        return -1


print(solution(121))