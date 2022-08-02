answer = 0

def dfs(k, depth, dungeons, visited):
    global answer
    if depth > answer:
        answer = depth
    if answer == len(dungeons):
        return

    for i in range(len(dungeons)):
        # visitedIvalue = visited[i]
        # dun0Value = dungeons[i][0]
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], depth + 1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]
#dungeons = [[20,20],[80,20],[50,40],[70,35],[30,10]]
print(solution(k, dungeons))