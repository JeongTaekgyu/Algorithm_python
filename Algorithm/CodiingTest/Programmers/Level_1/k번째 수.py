def solution(array, commands):
    answer = []
    tmp = []

    for com in commands:
        for j in range(com[0]-1,com[1]):
            tmp.append(array[j])
        tmp.sort()
        answer.append(tmp[com[2]-1])
        tmp.clear() # 리스트의 모든 요소 제거

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))