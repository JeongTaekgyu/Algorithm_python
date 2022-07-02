def solution(prices):
    answer = []
    cnt = 0
    chk = 0

    for i in range(len(prices)):
        cnt = 0
        chk = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                answer.append(cnt)
                chk = 1
                break
        if chk == 0:
            answer.append(cnt)

    return answer

prices = [3, 3, 7, 2, 3]
print(solution(prices))