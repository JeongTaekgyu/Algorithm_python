import heapq

# 내림차순 힙 정렬(heap sort)
def heapsort(list):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in list:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

list = [1,3,5,7,9,2,4,6,8,0]
result = heapsort(list)
print(result)