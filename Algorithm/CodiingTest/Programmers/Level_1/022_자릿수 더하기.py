import math


def solution(n):
    # 방법1
    # sum = 0

    # while n:
    #     sum = sum + (n % 10)
    #     n = math.floor(n / 10) # floor는 반 내림 함수

    #return sum

    # 방법2 - 이게 실행시간이 더 많이 걸린다..
    # n을 문자열로 바꿔서 list() 함수에 담으면 각 자리수를 분리해서 리스트로 담을 수 있다.
    # 그리고 map() 함수를 사용하면 입력되는 리스트들에 모두 일정한 함수를 적용시킬 수 있는데,
    # 무슨 말이냐면 코드에서 map(int, list)를 하면 list에 있는 모든 요소를
    # int() 함수에 넣은 결과값과 같다는 것이다.

    return sum(map(int, list(str(n))))


print(solution(987))