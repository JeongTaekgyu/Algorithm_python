def solution(num):
    # cnt = 0
    #
    # while(num != 1):
    #     cnt += 1
    #     if num % 2 == 0:
    #         num /= 2
    #     else:
    #         num = (num * 3) + 1
    #
    #     if cnt == 500:
    #         return -1
    #
    # return cnt


    # 테스트 13이 안된다. -> 이거 다른 사람 코드로 해도 안된다.
    for i in range(500):
        if num % 2 == 0:
            num /= 2
        else:
            num = (num * 3) + 1

        if num == 1:
            return i + 1

    return -1


print(solution(16))