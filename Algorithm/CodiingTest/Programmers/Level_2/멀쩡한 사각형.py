from math import gcd

def solution(w,h):
    return     w*h - (w+h - gcd(w,h))

w = 8
h = 12
print(solution(w,h))