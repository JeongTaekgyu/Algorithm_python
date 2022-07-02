input = 17


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!

    array = [True] * number

    sqrt = int(number ** 0.5)
    for i in range(2, sqrt + 1):   # 제곱근 까지
        if array[i] == True:    # i가 소수이면
            for j in range(i+i, number, i): # i이후 i(소수)의 배수들을 False 판정 range(초기값 ,끝값, 증감)
                array[j] = False

    print([i for i in range(2, number) if array[i] == True] )

    return [i for i in range(2, number) if array[i] == True]

result = find_prime_list_under_number(input)
print(result)