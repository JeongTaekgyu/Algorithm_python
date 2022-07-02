def solution(n, lost, reserve):
    answer = 0

    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for resv in set_reserve:
        if resv-1 in set_lost:  # 왼쪽 먼저 검사
            print('-1 : ', resv-1)
            set_lost.remove(resv-1) # 왼쪽에 있는애 체육복 줘야되니까 제거함
        elif resv+1 in set_lost:
            print('+1 : ', resv+1)
            set_lost.remove(resv+1) # 오른쪽에 있는애 체육복 줘야되니까 제거함

    answer = n - len(set_lost)
    return answer

n = 7
lost = [1,2,4]
reserve = [3,5]

print(solution(n, lost, reserve))