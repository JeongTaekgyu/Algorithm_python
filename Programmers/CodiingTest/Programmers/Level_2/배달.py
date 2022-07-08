import heapq
INF = int(1e9)

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N+1)

    for i in range(len(road)):
        a = road[i][0]
        b = road[i][1]
        c = road[i][2]
        graph[a].append((b,c))
        graph[b].append((a,c))

    q = []
    start = 1
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

    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
        if distance[i] != INF:
            print(i , ' : ', distance[i])

    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))

