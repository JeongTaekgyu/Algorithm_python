import heapq


def solution(operations):
    min_heap = []
    max_heap = []

    for ch in operations:
        command = ch.split(' ')

        if command[0] == 'I':
            num = int(command[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        else:
            if len(min_heap) == 0:
                pass
            elif command[1] == '1':
                maxValue = heapq.heappop(max_heap)[1]
                min_heap.remove(maxValue)
            elif command[1] == '-1':
                minValue = heapq.heappop(min_heap)
                max_heap.remove((-minValue, minValue))

    if min_heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        return [0,0]


operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))