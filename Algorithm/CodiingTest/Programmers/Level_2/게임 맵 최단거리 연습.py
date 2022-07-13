from collections import deque


def solution(maps):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

    graph = [[-1 for _ in range(c)] for _ in range(r)]
    print('1: ',len(graph))
    print('2: ',len(graph[0]))

    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1 # 처음은 1

    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1 # 이전 거에다 + 1
                    queue.append([ny, nx])

    answer = graph[r-1][c-1]    # 목적지 못가면 -1을 받환하고 목적지 가면 목적지 간만큼을 반환한다.
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,1,1]]
print(solution(maps))
