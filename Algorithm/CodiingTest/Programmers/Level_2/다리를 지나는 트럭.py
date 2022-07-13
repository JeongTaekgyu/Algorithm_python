def solution(bridge_length, weight, truck_weights):
    answer = 0
    cnt = 0
    #queue = [0 for i in range(bridge_length)]   #bridge_length 길이만큼 0으로 초기화
    queue = [0] * bridge_length

    while queue:
        cnt += 1
        queue.pop(0)

        if len(truck_weights) > 0:
            tmp = sum(queue) + truck_weights[0]
            if tmp <= weight:
                t = truck_weights.pop(0)
                queue.append(t)
            else:
                queue.append(0)

    answer = cnt
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))