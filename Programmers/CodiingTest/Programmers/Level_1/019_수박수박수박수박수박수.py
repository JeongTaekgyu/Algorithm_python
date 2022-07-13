def solution(n):
    # answer = ''
    #
    # for i in range(n):
    #     if i % 2 == 0:
    #         answer += '수'
    #     else:
    #         answer += '박'
    #
    # return answer

    s = "수박" * n
    print(s)
    return s[:n]    # 문자열 앞에서 원하는 글자수 만큼 자르기 앞에 0은 생략 가능

print(solution(3))