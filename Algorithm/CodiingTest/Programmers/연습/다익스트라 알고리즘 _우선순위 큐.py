import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))  # 시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0  # 시작노드->시작노드 거리 기록

    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 꺼낸 원소의 거리가 현재 테이블에 기록되어 있는 거리보다 크다면
        # 방문 처리돼 있는 노드라고 간주 할 수 있으므로 무시하면 된다.
        # (현재 노드가 이미 처리된 적이 있는 노드라면 무시)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next in graph[now]:
            # cost = 현재 확인하고 있는 노드의 거리 값 + 그 노드와 인접한 다른 노드의 거리값
            cost = dist + next[1]   # dist는 저장 되어있는 최단경로, next[1]은 다른 노드로 가는 거리 값
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next[0]]:
                distance[next[0]] = cost    # 작은 비용으로 거리를 갱신한다
                heapq.heappush(q, (cost, next[0]))  # 값이 갱신되면 우선순위큐에 넣는다

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 도달할 수 없다고라고 출력
    if distance[i] == INF:
        print('도달할 수 없음')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

# 아래는 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2