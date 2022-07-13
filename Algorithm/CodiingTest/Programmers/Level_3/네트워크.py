# def dfs(n, computers, start, visited):
#     visited[start] = True
#
#     for i in range(0, n):
#         if(visited[i] == False and computers[start][i] == 1):
#             visited = dfs(n, computers, i, visited)
#     return visited  # 반환값이 visited인가 잘 이해가 안가네

def dfs(n, computers, start, visited):
    visited[start] = True

    for i in range(0, n):
        if(visited[i] == False and computers[start][i] == 1):
            dfs(n, computers, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for start in range(0, n):
        if(visited[start] == False):
            dfs(n, computers, start, visited)
            answer += 1

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))