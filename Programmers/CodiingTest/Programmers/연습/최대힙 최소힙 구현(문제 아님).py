import heapq


def solution(numlist):

    heap = []

    for num in numlist:
        heapq.heappush(heap, (-num, num))   # 최대힙

    print(heap)
    print(heap[0])

    heap.remove((-3,3))
    print(heap)

numlist = [6,3,8,9,2,7,3]
solution(numlist)