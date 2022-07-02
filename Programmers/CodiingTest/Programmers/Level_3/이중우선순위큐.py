import heapq

def solution(operations):

    min_heap = []
    max_heap = []

    for op in operations:
        command = op.split(' ')
        if command[0] == 'I':
            num = int(command[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        else:
            if len(min_heap) == 0:
                pass
            elif command[1] == '1': # 최대값을 제거
                max_value = heapq.heappop(max_heap)[1]
                min_heap.remove(max_value)
            elif command[1] == '-1': #최소값을 제거
                min_value = heapq.heappop(min_heap)
                max_heap.remove((-min_value, min_value))

    if min_heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        return [0,0]


operations = ["I 7","I 5","I -5","D -1"]
print(solution(operations))