def bfs(y, x):
    queue = []
    queue.append((y,x))

    while queue:
        now = queue.pop(0)
        for i in range(4):
            nx = now[1] + dx[i]
            ny = now[0] + dy[i]
            if(0 <= ny < N) and (0 <= nx < M) and maps[ny][nx] == 1: # 범위에 있고 방문 하지 않은 곳이면
                maps[ny][nx] = -1
                queue.append((ny, nx))


T = int(input())

for _ in range(T):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # M : 가로 길이, N : 세로 길이
    M, N, K = map(int, input().split())
    # 배추밭 생성 ( N행 M열 )
    maps = [[0] * M for i in range(N)]
    cnt = 0

    for i in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1

    for i in range(N):  # 행
        for j in range(M):  # 열
            if maps[i][j] == 1: # 방문하지 않은 곳이면
                maps[i][j] = -1  # 방문 한곳을 표시    # 이게 있어야 시간이 좀더 단축되네
                bfs(i, j)
                cnt += 1

    for m in maps:
        print(m)
    print(cnt)