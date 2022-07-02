def solution(a, b):
    sum = 0

    if a <= b:
        for num in range(a, b + 1):
            sum += num
    else:
        for num in range(b, a + 1):
            sum += num

    return sum

#    if a > b:
#        t = a
#        a = b
#        b = t

#    print(a)
#    print(b)

#    return sum(range(a,b+1))

print(solution(3,-100))