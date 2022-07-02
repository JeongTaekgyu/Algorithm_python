def gcd(a, b):
    # a, b 의 크기와 상관없네
    # 1. a > b 이면 다이렉트로 계산되고
    # 2. a < b 이면 a가 b값이 되고 b가 a%b값이 된다.
        # 즉 a= 18, b= 63이면 a가 63이 되고 b가 18%63 -> 18 이된다.
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(n, m):
    answer = []

    answer.append(gcd(n,m))
    answer.append(lcm(n,m))

    return answer

n = 18
m = 63
print(solution(n, m))

# n, m = m , n
# print(n, m)