import heapq
from sys import stdin

n = int(stdin.readline())
heap = []

for _ in range(n):
    num = int(stdin.readline())

    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print('0')
    else:
        heapq.heappush(heap,[-num, num]) # 최대힙
    # heapq 모듈은 최소 힙(min heap)을 기능만을 동작하기 때문에 최대 힙(max heap)으로 활용하려면 약간의 요령이 필요하다.
    # 바로 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하는 것이다.
    # 따라서, 최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, (우선 순위, 값) 구조의 튜플(tuple)을 힙에 추가하거나 삭제하면 된다.
