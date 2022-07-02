def solution(N, stages):
    answer = []
    failureRate = {}
    denominator = len(stages)

    for i in range(1,N+1):
        if denominator != 0:
            failureRate[i] = stages.count(i) / denominator
            denominator -= stages.count(i)
        else:   # 분모가 0 이라는 것은 이미 count를 다 해서 count할게 없다는 것 그러므로 실패율은 0이다.
            failureRate[i] = 0

    #print(failureRate)
    # 딕셔너리를 키값 역순으로 정렬하기 ( 당연히 value도 key와 쌍을 이뤄서 정렬된다 )
    # 출처 : https://blockdmask.tistory.com/566
    tmp = sorted(failureRate.items(), key=lambda x: x[1], reverse=True)
    #print(tmp)

    for t in tmp:
        answer.append(t[0])

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))