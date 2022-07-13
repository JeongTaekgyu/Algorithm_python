def solution(n):
    # 방법1
    answer = []

    s = reversed(str(n))

    for i in s:
        answer.append(int(i))

    return answer

    # 방법2 - 각 자리수를 리스트로 변환하는 방법 - 시간 더 걸린다.
    #return list(map(int, reversed(str(n))))

print(solution(123))