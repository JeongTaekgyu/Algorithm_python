def bfs(y, x, N, M):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = []
    queue.append((y,x))
    cnt = 0
    min = N * M

    while queue:
        cnt += 1
        now = queue.pop(0)

        for i in range(4):
            nx = now[1] + dx[i]
            ny = now[0] + dy[i]
            if (0 <= ny < N) and (0 <= nx < M) and maps[ny][nx] == 1:
                maps[ny][nx] = -1
                queue.append((ny, nx))
                if nx+1 == M and ny+1 == N: # 종료지점에 도달하면
                    if cnt < min:
                        min = cnt
                    
    return min

def solution(maps):
    answer = 0
    cnt = 0

    cnt = bfs(0, 0, len(maps), len(maps[0]))

    #for i in range(len(maps)):
    #    for j in range(len(maps[i])):
    #        if maps[i][j] == 1: # 방문하지 안은 곳이면
    #            maps[i][j] = -1 # 방문 표시
    #            cnt = bfs(i, j, len(maps), len(maps[i]))

    print('cnt : ', cnt)
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,0,1]]
print(solution(maps))