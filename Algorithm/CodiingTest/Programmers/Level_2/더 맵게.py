import heapq


def solution(scoville, K):
    cnt = 0
    heap = []

    for num in scoville:
        heapq.heappush(heap, num)
    # print(len(heap))
    # print(len(scoville))
    # print('최소값? : ', heap[0])
    # print('~~~ ', len(heap))

    while heap[0] < K:
        if len(heap) == 1:
            return -1

        min = heapq.heappop(heap)
        secondMin = heapq.heappop(heap)
        heapq.heappush(heap, min+(secondMin*2))
        cnt += 1

    return cnt

scoville = [2, 10, 3, 9, 1, 12]
k = 7
print(solution(scoville, k))