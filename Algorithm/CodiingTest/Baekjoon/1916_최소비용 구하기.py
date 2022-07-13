import sys
import heapq
input = sys.stdin.readline  # 이거 없으면 시간 초과 난다.

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)


for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start ,end= map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for next in graph[now]:
            cost = dist + next[1]

            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


dijkstra(start)

print(distance[end])