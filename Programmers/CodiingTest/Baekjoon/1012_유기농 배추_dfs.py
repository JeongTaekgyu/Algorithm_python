
def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # map[행][렬] 때문에 nx,ny의 범위를 이렇게 지정함
        if(0 <= ny < N) and (0 <= nx < M):
            if maps[ny][nx] == 1:   # 방문안한 곳이면
                maps[ny][nx] = -1   # 방문한 곳으로 표시
                dfs(ny,nx)


T = int(input())

for _ in range(T):
    # M : 가로 길이, N : 세로 길이
    M, N, K = map(int, input().split())
    # 배추밭 생성 ( N행 M열 )
    maps = [[0] * M for i in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1

    cnt = 0

    for i in range(N):  # 행
        for j in range(M):  # 열
            if maps[i][j] > 0:
                dfs(i, j)
                cnt += 1

    # print('-----------')
    for m in maps:
         print(m)
    print(cnt)

