def bfs(y, x):
    queue = []
    queue.append((y,x))

    while queue:
        now = queue.pop(0)
        for i in range(4):
            nx = now[1] + dx[i]
            ny = now[0] + dy[i]

            if( 0 <= nx < M and 0 <= ny < N and matrix[ny][nx] == 1):
                matrix[ny][nx] = -1 # 방문함을 표시
                queue.append((ny,nx))


T = int(input())

for _ in range(T):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # M : 가로길이, N : 세로길이, K : 배추 위치 입력할 개수
    M, N, K = map(int, input().split())

    matrix = [[0] * M for i in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    cnt = 0
    for i in range(N):  # N :행
        for j in range(M):  # M: 열
            if matrix[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)