def solution(s):
    answer = ''
    center = int(len(s) / 2)
    if len(s) % 2 != 0:
        answer = s[center]
    else:
        answer = s[center - 1: center + 1]
    # 파이썬 슬라이싱은 start : end 인경우 end-1 까지 리턴한다
    return answer


print(solution("azbcsd"))
