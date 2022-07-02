def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zeroCnt = 0

    for num in lottos:
        if num == 0:
            zeroCnt += 1
        if num in win_nums:
            cnt += 1


    if cnt + zeroCnt == 6:
        answer.append(1)
        answer.append(1 + zeroCnt)
    elif cnt + zeroCnt == 5:
        answer.append(2)
        answer.append(2 + zeroCnt)
    elif cnt + zeroCnt == 4:
        answer.append(3)
        answer.append(3 + zeroCnt)
    elif cnt + zeroCnt == 3:
        answer.append(4)
        answer.append(4 + zeroCnt)
    elif cnt + zeroCnt == 2:
        answer.append(5)
        answer.append(5 + zeroCnt)
    else:
        answer.append(6)
        answer.append(6)

    if answer[1] == 7:
        answer[1] = 6

    return answer

lottos = [0, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 41, 4, 35]
print(solution(lottos,win_nums))